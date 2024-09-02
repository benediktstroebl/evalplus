from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_value: int = 0
    result: List[int] = []

    for number in numbers:
        max_value = max_value if max_value > number else number
        result.append(max_value)

    return result

