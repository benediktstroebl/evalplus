from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []
    length = len(numbers)
    i = 0
    while i < length:
        j = i
        while j < length:
            if numbers[j] > numbers[j - 1]:
                j += 1
            else:
                break
        result.append(numbers[j - 1])
        i = j
    return result

