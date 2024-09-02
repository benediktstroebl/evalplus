from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max: List[int] = []
    for index, number in enumerate(numbers):
        rolling_max.append(number)
        for prev_number in numbers[index:]:
            if prev_number > number:
                break
            else:
                rolling_max.append(prev_number)
                number = prev_number
    return rolling_max

