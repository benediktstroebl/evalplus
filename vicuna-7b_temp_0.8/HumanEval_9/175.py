from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = max(numbers)
    current_numbers = numbers[:]
    for i in range(1, len(numbers)):
        if numbers[i] == current_max:
            current_numbers = numbers[:i]
            break
        current_max = max(numbers[i:i + 1])
    return current_numbers

