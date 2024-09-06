from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    given moment in the sequence. Returns empty list if rolling_max_window is empty."""
    return list(map(max, window(numbers, rolling_max_window)))