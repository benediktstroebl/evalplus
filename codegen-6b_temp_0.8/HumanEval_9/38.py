from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    
    for i in range(len(numbers)):
        if i == 0:
            rolling_max_list.append(numbers[i])
        else:
            curr_max = max(numbers[i], rolling_max_list[i - 1])
            rolling_max_list.append(curr_max)

    return rolling_max_list
