from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    def helper(numbers, current_max, window_size):
        if window_size == 0:
            return [current_max]
        else:
            window_start = 0
            window_end = 1
            for i in range(window_size):
                window_end = (i + 1) % len(numbers)
                if numbers[window_start:window_end] == numbers[window_start:window_end]:
                    window_start += 1
                    window_end += 1
                else:
                    if window_end == len(numbers):
                        return [numbers[window_start:current_max + 1]]
                    window_max = max(numbers[window_start:window_end])
                    numbers[window_start:window_end] = [window_max]
                    window_start += 1
            return helper(numbers, current_max + 1, window_size - 1)
    return helper(numbers, 0, len(numbers) - 1)

