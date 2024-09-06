from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # initialize empty list and current index
    result = []
    current_index = 0

    # iterate through the sequence
    for i in range(len(numbers) - 1):
        # if the current element is greater than the previous max, reset max and move the current index to the end
        if numbers[i] > numbers[current_index]:
            result.append(numbers[current_index])
            current_index = len(numbers) - 1
        # add the current element to the list
        result.append(numbers[i])

    # append the last element to the list
    result.append(numbers[current_index])

    return result