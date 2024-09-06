from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Create a list to store the result
    max_list: List[int] = []
    for index in range(len(numbers)):
        if index == 0:
            # If this is the first iteration, append the first element
            max_list.append(numbers[index])
            continue
        if numbers[index] > max_list[index - 1]:
            # If the element is bigger than the last element on the max_list, append it.
            max_list.append(numbers[index])
        else:
            # If the element is smaller than the last element on the max_list, append the last element on the
            # max_list
            max_list.append(max_list[index - 1])
    return max_list

