from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    moment in the sequence. Optionally, specify the rolling maximum window size."""
    windows = collections.defaultdict(list)
    result = []
    # Record the rolling max in windows of size rolling_max_window
    for i, num in enumerate(numbers):
        for j in range(rolling_max_window):
            if j == 0:
                windows[j].append(num)
            else:
                windows[j].append(max(windows[j-1]))
        result.append(max(windows[-1]))
    return result