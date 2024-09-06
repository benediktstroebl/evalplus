from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('inf')] * rolling_window

    max_list = [float('inf')] * rolling_window
    max_list[0] = numbers[0]

    for i in range(1, len(numbers)):
        for j in range(rolling_window - 1):
            if numbers[i] > numbers[i - j - 1]:
                max_list[j] = numbers[i - j - 1]
        max_list[rolling_window - 1] = max(numbers[i], max_list[rolling_window - 1])

    return max_list