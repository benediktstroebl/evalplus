from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Make a sorted copy of the list
    numbers = sorted(numbers)

    # Get the maximum and its index
    max_num = numbers[-1]
    max_ind = len(numbers) - 1

    # Initialize result
    result = []

    # Loop over the numbers
    for i in range(len(numbers)):
        # If the number is greater than the max_num, update the max_element and max_index
        if numbers[i] > max_num:
            max_num = numbers[i]
            max_ind = i
        result.append(max_num)

    return result

