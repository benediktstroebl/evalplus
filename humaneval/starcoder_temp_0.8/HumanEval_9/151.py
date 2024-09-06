from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    def roll_max(prevs: Tuple[int,...], curr: int) -> Tuple[int,...]:
        return prevs[1:] + (max(prevs[0], curr),)

    return reduce(roll_max, numbers, (0,))[1:]

