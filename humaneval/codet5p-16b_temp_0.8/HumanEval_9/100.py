from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []
    last_max = numbers[0]
    for number in numbers:
        if number > last_max:
            result.append(number)
            last_max = number
        else:
            result.append(last_max)
    result.append(last_max)
    return result

