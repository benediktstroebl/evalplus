from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment in the sequence.

    Args:
        numbers (List[int]): The list of integers to process.
        rolling_window (int): The size of the rolling maximum window.

    Returns:
        List[int]: A list of integers representing the rolling maximum elements within the specified window.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    # Sort the input list in ascending order
    sorted_numbers = sorted(numbers)

    # Calculate the rolling maximum using a sliding window approach
    rolling_max_values = [sorted_numbers[0]]
    for i in range(1, len(sorted_numbers)):
        current_max = sorted_numbers[i]
        if i - rolling_window >= 0:
            current_max = max(current_max, sorted_numbers[i - rolling_window])
        rolling_max_values.append(current_max)

    # Reverse the list to get the desired order of rolling maximum elements
    reversed_rolling_max = rolling_max_values[::-1]

    # Return the reversed list if the window size is greater than the input list length, or an empty list otherwise
    return reversed_rolling_max[:len(reversed_rolling_max) if len(reversed_rolling_max) > len(numbers) else 0]