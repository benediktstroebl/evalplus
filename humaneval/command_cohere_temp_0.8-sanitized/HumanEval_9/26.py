from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    
    Args:
        numbers (List[int]): The list of integers to process.
        rolling_window (int): The rolling window size to consider at each moment.
    
    Returns:
        List[int]: A list of integers representing the rolling maximum elements found until the given moment.
    """
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [num for num in numbers]

    rolling_max_values = [num for num in numbers]
    for i in range(1, len(numbers) - rolling_window + 1):
        current_window = numbers[i-rolling_window:i+1]
        rolling_max_values[i] = max(current_window)

    return rolling_max_values