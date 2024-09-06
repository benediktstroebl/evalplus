from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # the first element is always the maximum
    max_num = numbers[0]
    result = []
    # iterate all the items in the sequence and append the rolling maximum
    for num in numbers:
        result.append(max_num)
        max_num = max(num, max_num)
    return result

