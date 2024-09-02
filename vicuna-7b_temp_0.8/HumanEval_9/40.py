from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    total_list = []
    current_max = None
    current_index = 0
    for i in range(len(numbers)):
        if numbers[i] > current_max:
            current_max = numbers[i]
            current_index = i
        total_list.append(current_max)
        current_max = None
    total_list.append(current_max)  # final max element
    return total_list

