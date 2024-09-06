from typing import List, Tuple
def rolling_max(numbers: List[int], window_size: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment in the sequence.

    Args:
        numbers (List[int]): List of integers to consider.
        window_size (int): Size of the rolling window.

    Returns:
        List[int]: List of maximum elements seen within the rolling window until the current moment.

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2], 2)
        [1, 2, 3, 3, 3, 4, 4]

        >>> rolling_max([1, 3, 2, 4, 4, 2, 1], 3)
        [1, 3, 3, 4, 4, 4, 2]
    """

    if not numbers or not isinstance(numbers, List) or not all(isinstance(n, int) for n in numbers):
        raise ValueError("Input 'numbers' must be a valid list of integers.")

    if not isinstance(window_size, int) or window_size <= 0:
        raise ValueError("Input 'window_size' must be a positive integer.")

    result = []
    max_seen = numbers[0]
    window = numbers[:window_size]

    for num in numbers[1:]:
        if num > max_seen:
            max_seen = num
        window.append(num)

        if max_seen >= window[0]:
            result.append(max_seen)

        window.pop(0)

    return result