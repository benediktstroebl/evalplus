from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []

    if len(numbers) <= 1:
        return numbers

    result.append(numbers[0])
    max_so_far = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > max_so_far:
            result.append(numbers[i])
            max_so_far = numbers[i]
        else:
            result.append(max_so_far)

    return result

