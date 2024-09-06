from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[1]) for _ in range(len(numbers) - rolling_window + 1)]