from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the current moment in the sequence."""
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('inf')] * rolling_window

    max_indices = []  # To store indices of maximum elements encountered so far
    max_element = float('-inf')  # To track the maximum element encountered so far

    for i, num in enumerate(numbers):
        # Update rolling maximum if the current element is greater
        if num > max_element:
            max_element = num
            max_indices = [i]  # Update the index for the rolling max

        # Update the rolling window of maximum elements
        if len(max_indices) < rolling_window:
            max_indices.append(i)
        else:
            max_indices[0] = i  # Update the first element of the rolling max window

        # Remove elements from the rolling window that fall outside the current window
        max_indices[:] = max_indices[-rolling_window :]

    return [num for num in numbers if num == max_element or num == max_indices[0]]
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3