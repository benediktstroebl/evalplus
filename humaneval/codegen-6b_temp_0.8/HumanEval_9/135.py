from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    length = len(numbers)
    maximum = numbers[0]
    result = [maximum]
    index = 0
    for i in range(1, length):
        if numbers[i] > maximum:
            maximum = numbers[i]
            index = i
        else:
            result.append(maximum)
    result.append(maximum)
    return result

