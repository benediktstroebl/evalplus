from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_ = numbers[0]
    result = [max_]
    for num in numbers[1:]:
        if num > max_:
            result.append(num)
            max_ = num
        else:
            result.append(max_)
    return result

