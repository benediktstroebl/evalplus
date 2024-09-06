from typing import List, Tuple
def rolling_max(numbers: List[int], optional_window_size: int = 1) -> List[int]:
    if not numbers:
        return []

    if optional_window_size <= 0:
        return [max(numbers)]

    window_size = optional_window_size
    max_so_far = max(numbers[:window_size])
    result = [max_so_far]

    for i in range(window_size, len(numbers)):
        max_so_far = max(numbers[i-window_size:i+1])
        result.append(max_so_far)

    return result