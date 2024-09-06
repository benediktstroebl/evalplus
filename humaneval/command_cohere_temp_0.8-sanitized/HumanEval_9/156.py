from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    given moment in the sequence. Maximum elements overlapping with the rolling_max_window are included."""
    return [max(numbers[i - rolling_max_window:i + 1]) for i in range(len(numbers) - rolling_max_window + 1)]