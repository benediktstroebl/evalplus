from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    given moment in the sequence."""
    if not numbers:
        return []

    if rolling_max_window <= 0:
        return [min(numbers)]

    curr_max = max(numbers[0:rolling_max_window])
    result = [curr_max] * rolling_max_window

    for idx, num in enumerate(numbers[rolling_max_window:]):
        if num > curr_max:
            curr_max = num
            result[idx - rolling_max_window] = curr_max

    return result
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_window = 3
result = rolling_max(numbers, rolling_max_window)