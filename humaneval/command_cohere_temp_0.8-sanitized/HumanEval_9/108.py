from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

    Args:
        numbers (List[int]): The list of integers to process.
        rolling_window (int): The size of the rolling maximum window.

    Returns:
        List[int]: A new list where each element is the maximum of the current window.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers or not rolling_window:
        return []

    # Create a buffer to store the rolling window of integers, initialized with the first `rolling_window` integers from `numbers`.
    buffer = [numbers[0]]
    buffer.extend(numbers[1:rolling_window])

    for i in range(rolling_window, len(numbers)):
        # Add the current integer to the buffer and remove the oldest integer to maintain the rolling window.
        buffer.append(numbers[i])
        buffer.pop(0)

        # Update the maximum if the current integer is greater than the maximum in the buffer.
        if numbers[i] > buffer[0]:
            buffer[0] = numbers[i]

    # Return the buffer, which now holds the rolling maximum for each position in `numbers`.
    return buffer