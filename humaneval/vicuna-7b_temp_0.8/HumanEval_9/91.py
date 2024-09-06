from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    window_size = 5  # Example: rolling window of 5 numbers
    for i in range(len(numbers) - window_size):
        window = numbers[i:i + window_size]
        max_value = max(window)
        result.append(max_value)
    return result