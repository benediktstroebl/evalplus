from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_number = numbers[0]
    result = [max_number]  # type: List[int]
    for num in numbers:
        if num > max_number:
            max_number = num
            result.append(max_number)
        else:
            result.append(max_number)
    return result[1:]

