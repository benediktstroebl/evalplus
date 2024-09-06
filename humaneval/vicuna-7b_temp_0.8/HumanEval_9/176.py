from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    for i in range(len(numbers) - 1):
        max_index = len(numbers) - 1
        max_value = numbers[-1]
        for j in range(i, len(numbers)):
            if numbers[j] >= max_value:
                max_index = j
                max_value = numbers[j]
        result.append(max_value)
    return result

