from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    return [max(numbers[i - rolling_max_window:i + 1]) for i in range(len(numbers))]