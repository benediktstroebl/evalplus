from typing import List, Tuple
def rolling_max(numbers: List[int], window_size: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers to process.
        window_size (int): The size of the rolling window.

    Returns:
        List[int]: A list of integers representing the rolling maximum elements within the specified window.
    """
    
    if not numbers:
        return []

    if len(numbers) < window_size:
        return numbers
    
    rolling_maxes = [numbers[0]]
    
    for i in range(1, len(numbers)):
        current_max = numbers[i]
        for j in range(i - window_size + 1, i):
            if numbers[j] > current_max:
                current_max = numbers[j]
        rolling_maxes.append(current_max)
    
    return rolling_maxes