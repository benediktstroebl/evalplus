from typing import List, Tuple
def rolling_max(numbers: List[int], max_window: int = None) -> List[int]:
    if not numbers or max_window and max_window <= 0:
        return []

    if max_window:
        window_size = max_window
    else:
        window_size = len(numbers)

    cur_max = numbers[0]
    result = [cur_max]

    if window_size > 1:
        maxes = [numbers[0]]
        for idx, num in enumerate(numbers[1:]):
            cur_max = max(num, cur_max)
            maxes.append(cur_max)
            result.append(maxes[-1])

    return result
numbers = [1, 2, 3, 2, 3, 4, 2]