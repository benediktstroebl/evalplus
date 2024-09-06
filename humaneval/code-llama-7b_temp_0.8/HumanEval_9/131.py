from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers: List[int] = []
    for number in numbers:
        if not max_numbers or max_numbers[-1] < number:
            max_numbers.append(number)
        else:
            max_numbers.append(max_numbers[-1])
    return max_numbers

