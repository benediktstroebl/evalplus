from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        raise ValueError("Empty sequence")
    i, j = 0, 1
    max_numbers = [numbers[i]]
    while j < len(numbers):
        if numbers[j] > max_numbers[-1]:
            max_numbers.append(numbers[j])
        else:
            max_numbers[-1] = numbers[j]
        j += 1
    return max_numbers

