from typing import List, Tuple
def rolling_max(numbers: List[int], window_size: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): List of integers.
        window_size (int): Window size to consider for computing the rolling maximum.

    Returns:
        List[int]: List of rolling maximum elements.
    """

    if not numbers:
        return []

    if window_size <= 0 or window_size > len(numbers):
        raise ValueError("Invalid window size. Window size must be positive and smaller than the "
                         "length of the input list.")

    max_heap = []  # Heap to efficiently find the rolling maximum
    heapq.heappush(max_heap, numbers[0])

    result = [numbers[0]]

    for i in range(1, len(numbers)):
        while max_heap and numbers[i] > max_heap[0]:
            prev_max = heapq.heappop(max_heap)
            result.append(prev_max)

        heapq.heappush(max_heap, numbers[i])

    # Add the last maximum element of the window
    result.append(heapq.heappop(max_heap))

    return result
numbers = [1, 2, 3, 2, 3, 4, 2]
window_size = 3
result = rolling_max(numbers, window_size)