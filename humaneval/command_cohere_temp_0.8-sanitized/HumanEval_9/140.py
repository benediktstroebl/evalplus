from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the current moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers to be processed.
        rolling_window (int): The rolling window size to look forward.

    Returns:
        List[int]: A list of integers representing the rolling maximum elements found.
    """

    # Initialize an empty list to store the rolling maximum elements
    result = []

    # Initialize variables to keep track of the previous maximum and its index
    prev_max = numbers[0]
    prev_max_idx = 0

    # Iterate through the list with a window of size 'rolling_window'
    for i in range(rolling_window, len(numbers)):
        # Get the maximum value between the previous maximum and the current element
        max_val = max(numbers[i - rolling_window:i + 1])
        curr_max_idx = i - rolling_window

        # If the current maximum is different from the previous one, add it to the result and update the variables
        if max_val != prev_max:
            result.append(max_val)
            prev_max = max_val
            prev_max_idx = curr_max_idx

    return result
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3
result = rolling_max(numbers, rolling_window)