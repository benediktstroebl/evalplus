from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """Return a list of rolling maximum elements from the given list of integers."""
    # Initialize a list to store the rolling maximum elements
    max_list = [float('-inf')] * rolling_window

    # Initialize a loop to iterate over the list of numbers
    for i, number in enumerate(numbers):
        # Update the list of rolling maximum elements
        update_max_list(i, number, rolling_window, max_list)

    # Return the final list of rolling maximum elements
    return max_list
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3