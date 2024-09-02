from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_len = len(numbers)
    max_num = max(numbers)
    max_index = numbers.index(max_num)
    result = [max_num] * max_index
    curr = max_num
    for i in range(max_index, max_len):
        if numbers[i] > curr:
            result.append(numbers[i])
            curr = numbers[i]
    return result

