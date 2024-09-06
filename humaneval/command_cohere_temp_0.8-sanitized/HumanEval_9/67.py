from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    if rolling_window <= 0:
        return numbers[:]

    # Initialize result and window variables
    result = [float('-inf')] * rolling_window
    window = numbers[:rolling_window]

    for i in range(rolling_window, len(numbers)):
        # Add the maximum value from the current window to the result
        result[i % rolling_window] = max(window[i % rolling_window], result[i % rolling_window])
        # Update the window with next value
        window[(i+1) % rolling_window] = numbers[i]

    return result