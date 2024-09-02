from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        raise ValueError("Cannot process empty input")
    result: List[int] = []
    rolling_max_num: int = numbers[0]
    for number in numbers:
        rolling_max_num = max(rolling_max_num, number)
        result.append(rolling_max_num)
    return result

