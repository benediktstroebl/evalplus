from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the current moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers to be processed.
        rolling_window (int): The rolling window size to consider while finding the rolling maximum.

    Returns:
        List[int]: A list of integers representing the rolling maximum elements found.
    """

    # Initialize an empty list to store the rolling maximum elements
    rolling_max_list = []

    # Initialize two pointers at the start of the provided list
    current_index = 0
    window_index = rolling_window - 1

    # Iterate through the provided list
    for num in numbers:
        # If the current element is greater than the farthest element in the rolling window, update the farthest element
        if num > numbers[window_index]:
            rolling_max_list.append(num)
            window_index = (window_index + 1) % rolling_window

        # Move the current pointer one step ahead
        current_index = (current_index + 1) % rolling_window

    # Add the last rolling maximum element if it hasn't been added yet
    if numbers[current_index] > numbers[window_index]:
        rolling_max_list.append(numbers[current_index])

    return rolling_max_list
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3