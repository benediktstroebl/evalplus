from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    roll = []
    for element in numbers:
        if len(roll) == 0 or element >= roll[-1]:
            roll.append(element)
        else:
            roll.append(roll[-1])
    return roll

