from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(numbers[-rolling_window:]) for _ in range(len(numbers))]