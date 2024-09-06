from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    given moment in the sequence. If rolling_max_window is less than 1, then return a list of maximum
    elements for each element in the provided list."""
    
    # Create a list of maximum length rolling_max_window to initialize the rolling max values and initialize the variable to store the max value in the rolling window.
    result = [float('-inf')] * rolling_max_window
    max_in_window = float('-inf')
    
    # Create a list of the same length as rolling_max_window to store the current index to iterate through the list.
    window_indices = [0] * rolling_max_window
    
    # Iterate through the list and update the rolling max values accordingly.
    for i in range(len(numbers)):
        while window_indices[-1] <= i - rolling_max_window:
            window_indices.pop()
        if numbers[i] > max_in_window:
            max_in_window = numbers[i]
            window_indices[-1] = i
        for idx in window_indices:
            if numbers[idx] >= max_in_window:
                continue
            result[idx] = max_in_window
            if i >= rolling_max_window:
                result.pop(0)
            else:
                result.insert(0, max_in_window)
    return result