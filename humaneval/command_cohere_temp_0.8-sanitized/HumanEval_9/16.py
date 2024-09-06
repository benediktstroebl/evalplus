from typing import List, Tuple
def rolling_max(numbers: List[int], max_window: int = None) -> List[int]:
    if max_window is None:
        max_window = len(numbers)

    result = [num for num in numbers]
    for i in range(1, max_window):
        result[i] = max(result[i-1], result[i])

    return result