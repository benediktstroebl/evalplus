from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = max(numbers)
    current_max_index = 0
    rolling_max_list = [current_max]
    
    while True:
        for i in range(1, len(rolling_max_list)):
            if rolling_max_list[i] > rolling_max_list[i-1]:
                current_max = rolling_max_list[i]
                current_max_index = i
                rolling_max_list[current_max_index:] = [rolling_max_list[i+1] for i in range(len(rolling_max_list)-1, current_max_index-1, -1)]
                break
        else:
            break
    
    return rolling_max_list[current_max_index:]

