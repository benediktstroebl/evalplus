from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers_with_index = {i: i+1 for i in numbers}
    current_max = max(numbers_with_index.keys())
    current_numbers = numbers_with_index[current_max]
    return current_numbers

