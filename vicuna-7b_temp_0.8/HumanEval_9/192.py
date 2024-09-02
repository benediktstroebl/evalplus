from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Get the length of the input list
    n = len(numbers)
    # Create an empty list to store the rolling maximum values
    rolling_max_values = [0] * n
    # Initialize the rolling maximum value to the first element of the input list
    rolling_max_value = numbers[0]
    # Loop through each element in the input list
    for i in range(1, n):
        # Update the rolling maximum value with the current element
        rolling_max_value = numbers[i]
        # Add the current element to the rolling maximum values list
        rolling_max_values.append(rolling_max_value)
        # Move the rolling maximum value to the next position in the list
        rolling_max_value = numbers[i - 1]
    # Return the rolling maximum values list
    return rolling_max_values

