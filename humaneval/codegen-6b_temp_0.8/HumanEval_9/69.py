from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_numbers = [numbers[0]]
    for index in range(1, len(numbers)):
        if numbers[index] > max_numbers[-1]:
            max_numbers.append(numbers[index])
        else:
            max_numbers[-1] = numbers[index]
    return max_numbers

