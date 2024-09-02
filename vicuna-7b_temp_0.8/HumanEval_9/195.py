from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_count = 0
    max_value = None
    max_index = 0
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            max_index = 0
            max_value = num
        max_count += 1
        current_max = max_value
    return [max_value] + [current_max] * max_count

