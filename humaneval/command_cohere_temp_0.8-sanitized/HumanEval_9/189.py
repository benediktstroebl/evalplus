from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(numbers[i:i+rolling_window]) for i in range(len(numbers) - rolling_window + 1)]