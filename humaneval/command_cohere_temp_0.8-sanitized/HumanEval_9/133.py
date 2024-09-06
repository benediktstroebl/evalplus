from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

 Args:
    numbers (List[int]): List of integers to analyze
    rolling_window (int): Window size to consider to compute the maximum rolling value

 Returns:
    List[int]: List of maximum values at each window until the end of the sequence
>>> rolling_max([1, 2, 3, 2, 3, 4, 2], 2)
[1, 2, 3, 3, 3, 4, 4]
"""
    if not numbers or rolling_window <= 0:
        return []

    # Initialize an empty list to store the rolling maximum values (initially set to the first element of the input list)
    rolling_max_values: List[int] = [numbers[0]]

    # Initialize an empty list to store the indices where the rolling maximum values change (initially set to the first index)
    rolling_max_indices: List[int] = [0]

    # Iterate through the input list
    for i in range(1, len(numbers)):
        # Check if the current element is greater than the current rolling maximum value
        if numbers[i] > rolling_max_values[-1]:
            # If so, update the rolling maximum value and its index
            rolling_max_values.append(numbers[i])
            rolling_max_indices.append(i)
        else:
            # If not, check if the rolling window has been reached
            if i - rolling_max_indices[-1] >= rolling_window:
                # If so, update the rolling maximum value and its index
                rolling_max_values.append(numbers[i])
                rolling_max_indices.append(i)

    # Return the rolling maximum values up to the current moment
    return rolling_max_values[rolling_max_indices[-1]:]