from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > max_numbers[-1]:
            max_numbers.append(numbers[i])
        else:
            max_numbers.append(max_numbers[-1])
    return max_numbers

