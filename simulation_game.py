from enum import Enum, auto
import random

Vec2D = tuple[int, int]


class Floor(Enum):
    White = auto()
    Black = auto()


class Direction(Enum):
    North = auto()
    East = auto()
    South = auto()
    West = auto()

    Northeast = auto()
    Southeast = auto()

    Northwest = auto()
    Southwest = auto()


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


def get_new_pos(pos: Vec2D, direction: Direction) -> Vec2D:

    x, y = pos
    match direction:
        case Direction.North:
            return (x, y + 1)

        case Direction.South:
            return (x, y - 1)

        case Direction.West:
            return (x - 1, y)

        case Direction.East:
            return (x + 1, y)

        case Direction.Northeast:
            return (x + 1, y + 1)

        case Direction.Southeast:
            return (x + 1, y - 1)

        case Direction.Northwest:
            return (x - 1, y + 1)

        case Direction.Southwest:
            return (x - 1, y - 1)


def get_king_new_direction(king_pos: Vec2D) -> Direction:
    current_floor = get_chess_table_floor(king_pos)

    match current_floor:
        case Floor.White:
            return Direction.North
        case Floor.Black:
            directions = list(Direction)
            return random.choice(directions)


def initial_pos() -> Vec2D:
    return random.choice([(0, 0), (1, 0), (0, 1), (1, 1)])


def run_game(desired_directions: list[Direction]) -> bool:
    """
    Returns True if the king have the same directions of the desired directions list 
    """
    king_pos = initial_pos()

    total_movements = len(desired_directions)
    king_directions = []

    for i in range(total_movements):

        new_direction = get_king_new_direction(king_pos)

        if new_direction != desired_directions[i]:
            return False

        king_directions.append(new_direction)

        king_pos = get_new_pos(king_pos, new_direction)

    return True


def main() -> None:
    desired_directions = [
        Direction.North,
        Direction.South,
        Direction.South,
        Direction.North,

        Direction.Northeast,
        Direction.Southwest,
        Direction.Southwest,
        Direction.Northwest,

        Direction.Northwest,
        Direction.Southeast,
        Direction.Southeast,
        Direction.Northeast,
    ]

    number_of_trails = 1_000_000
    occurs = 0
    for i in range(number_of_trails):
        print(f"processing: {(i+1)*100/number_of_trails}% ", end="\r")
        if run_game(desired_directions):
            occurs += 1

    output_message = f'''
    number of trails: {number_of_trails}
    occurrences: {occurs}
    Probability: {occurs/number_of_trails}
    '''
    print(output_message)
    

if __name__ == '__main__':
    main()
