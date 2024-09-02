from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize empty list to store the rolling maximum elements
    rolling_max_list = []

    # Initialize a variable to store the current maximum element found in the sequence
    current_max = numbers[0]

    # Iterate through the sequence
    for i in range(len(numbers) - 1):
        # Calculate the rolling maximum element by finding the maximum of the sub-sequence starting from the current element
        rolling_max_element = max(numbers[i+1:i+2], key=lambda x: x if x > current_max else current_max)

        # Add the rolling maximum element to the list
        rolling_max_list.append(rolling_max_element)

        # Set the current maximum element to the current element
        current_max = numbers[i+1]

    # Add the last element of the sequence to the list
    rolling_max_list.append(current_max)

    return rolling_max_list
