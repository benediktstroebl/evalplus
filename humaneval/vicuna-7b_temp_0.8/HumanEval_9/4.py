from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Find the index of the maximum element in the list
    max_index = 0
    max_value = numbers[0]

    for number in numbers[1:]:
        if number > max_value:
            max_index = 0
            max_value = number
        else:
            max_index += 1

    # Initialize a list to store the rolling maximum elements
    rolling_max_list = [max_value]

    # Find the index of the maximum element in the current list
    max_index = 0
    max_value = numbers[0]

    for number in numbers[1:]:
        if number > max_value:
            max_index = 0
            max_value = number
        else:
            max_index += 1

    # Append the current maximum element to the rolling maximum list
    rolling_max_list.append(max_value)

    # Return the rolling maximum list
    return rolling_max_list

