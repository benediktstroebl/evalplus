from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the current moment
    in the sequence. Maximum elements overlapping with the rolling window are included."""
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('inf')] * rolling_window

    max_buffer = [float('inf')] * rolling_window
    max_buffer[0] = numbers[0]

    for i in range(1, len(numbers)):
        for j in range(rolling_window - 1):
            max_buffer[j] = max(max_buffer[j], numbers[i] >= max_buffer[j + 1])
        max_buffer[rolling_window - 1] = max(max_buffer[rolling_window - 1], numbers[i] >= numbers[i - rolling_window])

    return max_buffer