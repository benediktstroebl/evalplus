from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elements: List[int] = [None] * len(numbers)
    max_elements[0] = numbers[0]
    for i in range(1, len(numbers)):
        max_elements[i] = max(numbers[i], max_elements[i-1])
    return max_elements

