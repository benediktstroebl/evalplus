from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    
    Args:
        numbers (List[int]): The list of integers to process.
        rolling_window (int): The size of the rolling maximum window.
    
    Returns:
        List[int]: A new list containing the rolling maximum elements.
    """
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return numbers[:]

    rolling_maxes = [numbers[0]] + [float('-inf')] * rolling_window

    for i in range(1, len(numbers)):
        for j in range(i - rolling_window, i):
            if numbers[j] > rolling_maxes[j - i + 1]:
                rolling_maxes[j - i + 1] = numbers[j]

    return rolling_maxes[rolling_window:][:len(numbers) - rolling_window + 1]
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3