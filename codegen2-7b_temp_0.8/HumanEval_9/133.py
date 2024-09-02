from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_array = [0 for _ in range(len(numbers))]
    for i in range(len(numbers)):
        if i == 0 or numbers[i] > numbers[i - 1]:
            max_array[i] = numbers[i]
        else:
            max_array[i] = max(numbers[i], max_array[i - 1])
    return max_array
