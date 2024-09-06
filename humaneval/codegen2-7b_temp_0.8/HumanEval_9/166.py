from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_range = numbers[0]
    max_range_count = 1
    current_max = numbers[0]
    for number in numbers[1:]:
        if number > current_max:
            current_max = number
            max_range_count += 1
        else:
            current_max = max(current_max, number)
            max_range_count = 1
    return [max_range] * max_range_
