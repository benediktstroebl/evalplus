from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_index = 0
    max_value = numbers[0]
    rolling_max_list = [max_value]
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_index = i
            max_value = numbers[i]
            rolling_max_list = [max_value]
        else:
            rolling_max_list.append(max_value)
            max_value = numbers[i]
    return rolling_max_list[-1::-1]

