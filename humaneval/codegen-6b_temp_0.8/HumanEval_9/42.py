from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize arrays with initial conditions
    result: List[int] = [None] * len(numbers)
    max_number: int = numbers[0]
    max_index: int = 0
    result[0] = max_number

    for i in range(1, len(numbers)):
        if max_number < numbers[i]:
            max_number = numbers[i]
            max_index = i
        result[i] = max_number

    return result

