from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Check if input is a non-empty list
    if not numbers:
        return []

    # Initialize empty list for the rolling maximum elements
    rolling_max_list = [numbers[0]]

    # Initialize the rolling maximum element variable
    rolling_max_element = numbers[0]

    # Increment the index to move to the next element
    index = 0

    # Iterate over the list
    for i in range(1, len(numbers)):
        # Compare the current element with the rolling maximum element
        if numbers[i] > rolling_max_element:
            # If the current element is greater than the rolling maximum element, update the rolling maximum element
            rolling_max_element = numbers[i]
        # Append the current element to the rolling maximum list
        rolling_max_list.append(numbers[i])

    return rolling_max_list

