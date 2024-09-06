from typing import List, Tuple
def rolling_max(numbers: List[int], window_size: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    if window_size >= len(numbers):
        return numbers[:]

    result = [None] * window_size
    result[0] = numbers[0]
    for i in range(1, len(numbers)):
        for j in range(1, window_size):
            if numbers[i] > numbers[j]:
                result[j] = numbers[i]
        if i >= window_size - 1:
            result[window_size - 1] = numbers[i]

    return result
numbers = [1, 2, 3, 2, 3, 4, 2]