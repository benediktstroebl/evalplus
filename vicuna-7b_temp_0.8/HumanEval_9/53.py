from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Set the window size and the maximum element
    window_size = 2
    max_element = None
    max_index = 0

    # Initialize the rolling maximum list
    rolling_max_list = []

    # Iterate over the input list
    for i in range(len(numbers) - window_size):
        # Get the maximum element from the window
        max_element = numbers[i:i + window_size]
        max_index = len(max_element) - 1

        # Add the maximum element to the rolling maximum list
        rolling_max_list.append(max_element[max_index])

        # Update the maximum element
        if max_element[max_index] > max_element[max_index - 1]:
            max_element[max_index] = max_element[max_index - 1]
            max_index -= 1

        # Check if the maximum element is greater than the maximum element from the input list
        if max_element[max_index] > max_element[max_index - window_size]:
            max_element[max_index] = max_element[max_index - window_size]
            max_index -= window_size

    # Add the maximum element from the input list
    rolling_max_list.append(numbers[i])

    return rolling_max_list