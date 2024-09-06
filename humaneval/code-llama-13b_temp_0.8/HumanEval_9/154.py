from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maximum_num = numbers[0]
    result = [maximum_num]
    for i in range(1, len(numbers)):
        maximum_num = max(maximum_num, numbers[i])
        result.append(maximum_num)
    return result

