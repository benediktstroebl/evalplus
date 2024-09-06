from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

 Args:
    numbers (List[int]): List of integers to analyze
    rolling_window (int): Window size to consider to compute the maximum rolling value

 Returns:
    List[int]: A list of integers representing the rolling maximum seen up to each position while considering the window size.
 """
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [0] * len(numbers)

    rolling_maxes = [0] * (len(numbers) - rolling_window + 1)
    current_max = numbers[0]

    for i in range(rolling_window, len(numbers)):
        current_max = max(numbers[i], current_max, numbers[i - rolling_window])
        rolling_maxes[i - rolling_window] = current_max

    return rolling_maxes