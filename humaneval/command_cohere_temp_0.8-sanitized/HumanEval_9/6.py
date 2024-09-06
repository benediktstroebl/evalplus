from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers[-rolling_window:])) for nums in range(len(numbers))]