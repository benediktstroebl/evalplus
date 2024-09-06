from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('inf')] * rolling_window

    max_vals = [float('inf')] * rolling_window
    max_idx = 0

    for idx, num in enumerate(numbers):
        max_vals[max_idx] = num
        for i in range(rolling_window - 1, idx - 1, -1):
            if max_vals[i] < max_vals[i + 1]:
                max_vals[i + 1] = max_vals[i]
        max_idx = (max_idx + 1) % rolling_window

    return max_vals
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3