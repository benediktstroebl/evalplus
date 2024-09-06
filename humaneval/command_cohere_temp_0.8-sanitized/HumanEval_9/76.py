from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('inf')] * rolling_window

    max_buffer = [float('inf')] * rolling_window
    max_buffer[0] = numbers[0]
    result = [max_buffer[0]]

    for i in range(1, len(numbers)):
        for j in range(i - rolling_window + 1, i):
            if numbers[j] > max_buffer[j - i + 1]:
                max_buffer[j - i + 1] = numbers[j]
        result.append(max_buffer[0])

    return result