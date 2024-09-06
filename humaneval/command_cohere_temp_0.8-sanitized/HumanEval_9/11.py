from typing import List, Tuple
def rolling_max(numbers: List[int], optional_window_size: int = 1) -> List[int]:
    if not numbers:
        return []

    if optional_window_size == 1:
        return [max(numbers[i], numbers[i-1]) for i in range(1, len(numbers))]
    else:
        return [max(numbers[i-window_size:i+1]) for i in range(window_size, len(numbers))]
numbers = [1, 2, 3, 2, 3, 4, 2]