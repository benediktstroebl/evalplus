from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    curr_max = numbers[0]
    max_numbers = [numbers[0]]
    for number in numbers[1:]:
        curr_max = max(number, curr_max + number)
        max_numbers.append(curr_max)
    return max_numbers

