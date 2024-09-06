from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(range(i-rolling_window, i+1))) for i in range(len(numbers))]