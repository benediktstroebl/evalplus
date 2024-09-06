from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

    Args:
        numbers (List[int]): The list of integers to process.
        rolling_window (int): The size of the rolling maximum window.

    Returns:
        List[int]: A new list containing the rolling maximum seen at each position up to the current moment in the sequence.
    """
    if not numbers or rolling_window <= 0:
        return []

    result = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - rolling_window]:
            result[i] = numbers[i - rolling_window]
    return result