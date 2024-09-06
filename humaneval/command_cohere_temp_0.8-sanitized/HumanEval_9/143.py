from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(numbers[i - rolling_window:i]) for i in range(len(numbers))]