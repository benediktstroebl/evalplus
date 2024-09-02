from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result: List[int] = []
    for i in range(len(numbers)):
        curr_max: int = numbers[i]
        for j in range(i, len(numbers)):
            if numbers[j] > curr_max:
                curr_max = numbers[j]
        result.append(curr_max)
    return result

