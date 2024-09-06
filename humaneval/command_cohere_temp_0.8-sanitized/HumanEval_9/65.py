from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence. Implements the sliding window maximum algorithm."""
    if not numbers or not rolling_window:
        return []

    # Initialize the rolling maximum list with the first `rolling_window` elements
    max_list = [num for num in numbers[:rolling_window]]

    for current_num in numbers[rolling_window:]:
        # Update the rolling maximum list at the current index
        max_list[current_num % rolling_window] = max(current_num, max_list[current_num % rolling_window])

        # Return the current maximum for the next window
        yield max_list[current_num % rolling_window]