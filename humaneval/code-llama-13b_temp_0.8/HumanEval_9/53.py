from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [0] * len(numbers)
    current_max = numbers[0]
    result[0] = current_max
    for index, number in enumerate(numbers[1:]):
        index += 1
        if number > current_max:
            current_max = number
            result[index] = current_max
        else:
            result[index] = current_max
    return result

