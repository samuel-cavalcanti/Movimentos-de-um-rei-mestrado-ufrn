from enum import auto
from enum import Enum
import cv2
import numpy as np

Vec2D = tuple[int, int]


class Floor(Enum):
    White = auto()
    Black = auto()


def get_chess_table_floor(current_pos: Vec2D) -> Floor:

    x, y = current_pos
    rest = (x + y) % 2
    """The Formula was created drawing
       the chess table when pos 0,0 is black
    """

    if rest == 0:
        return Floor.Black
    else:
        return Floor.White


def create_chess_image_positive_values(shape: tuple) -> np.ndarray:
    new_image = np.zeros(shape, np.uint8)

    for j in range(shape[1]):
        for i in range(shape[0]):

            match get_chess_table_floor((i, j)):
                case Floor.Black:
                    new_image[i, j] = 0
                case Floor.White:
                    new_image[i, j] = 255

    return new_image

def create_chess_image_negative_values(shape: tuple) -> np.ndarray:
    new_image = np.zeros(shape, np.uint8)

    for j in range(shape[1]):
        for i in range(shape[0]):

            match get_chess_table_floor((-i, -j)):
                case Floor.Black:
                    new_image[i, j] = 0
                case Floor.White:
                    new_image[i, j] = 255

    return new_image

def main() -> None:

    resolution = (15, 15, 1)

    image_positive = create_chess_image_positive_values(resolution)
    image_negative = create_chess_image_negative_values(resolution)

    cv2.imwrite('chess_image_positive_values.png', image_positive)
    cv2.imwrite('chess_image_negative_values.png', image_negative)



if __name__ == '__main__':
    main()
