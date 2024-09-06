from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    assert len(numbers) > 0

    if len(numbers) == 1:
        return numbers

    # Length of the result list
    # Note: Tuple is a pair of values (value, index)
    result_len = len(numbers)
    # List of elements with their indices
    numbers_with_index = [(numbers[i], i) for i in range(len(numbers))]
    # The result
    result = []
    # Rolling maximum, e.g. find maximum number in [1, 2, 3]
    # Find rolling maximum number in [1, 2, 3, 2, 3, 4, 2]
    rolling_max_numbers = numbers_with_index[:3]
    # Initial max value
    rolling_max_numbers = sorted(rolling_max_numbers, key=lambda number: number[0])
    max_val = rolling_max_numbers[0][0]
    result.append(max_val)
    # Continue finding rolling maximum number in [1, 2
