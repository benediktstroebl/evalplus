from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_until_now = numbers[0]
    result = [max_until_now]
    for num in numbers:
        if num > max_until_now:
            max_until_now = num
            result.append(max_until_now)
        else:
            result.append(max_until_now)

    return result

