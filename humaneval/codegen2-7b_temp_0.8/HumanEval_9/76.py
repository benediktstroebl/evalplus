from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = numbers[0]
    roll_max = numbers[0]
    for number in numbers[1:]:
        if current_max < number:
            roll_max = current_max
            current_max = number
        else:
            current_max = number
    return [roll_max] + rolling_max(numbers[-1:])
