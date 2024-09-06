from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Check input
    if not isinstance(numbers, list) or not all(isinstance(number, int) for number in numbers):
        raise TypeError("Input must be list of integers")

    # Initialize solution
    result: List[int] = []
    max_value = numbers[0]

    # Perform rolling maximum
    for value in numbers[1:]:
        if value > max_value:
            max_value = value
        result.append(max_value)

    return result

