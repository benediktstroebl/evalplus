from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []

    for i, n in enumerate(numbers[1:]):
        current_max = numbers[i]
        for j in range(i, -1, -1):
            if numbers[j] > current_max:
                current_max = numbers[j]
        result.append(current_max)
    result.append(numbers[0])
    return result

