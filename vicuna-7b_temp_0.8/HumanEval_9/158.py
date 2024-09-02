from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 0
    max_num = max(numbers)
    result = [max_num]
    for i in range(1, len(numbers)):
        curr_max_num = max_num
        for j in range(i - n, len(numbers)):
            curr_max_num = max(curr_max_num, numbers[j])
        if curr_max_num == max_num:
            n += 1
        else:
            max_num = curr_max_num
            result.append(max_num)
        if curr_max_num == max_num:
            n += 1
    return result[n:]

