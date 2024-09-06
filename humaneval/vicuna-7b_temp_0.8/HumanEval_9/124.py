from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    result = numbers[:]
    index = 0

    while index < len(numbers) - 1:
        if numbers[index] > numbers[index+1]:
            result = [numbers[index]] + result[index+1:]
            index += 1
        else:
            result = result[index:]
            index += 1

    return result

