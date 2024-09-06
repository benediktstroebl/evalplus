from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    window_start, max_so_far = 0, float('-inf')
    result = [max_so_far] * len(numbers)
    for window_end in range(len(numbers)):
        max_so_far = max(max_so_far, numbers[window_end])
        if window_end - window_start == 1:
            result[window_end] = max_so_far
        else:
            result[window_end] = max(result[window_end], result[window_end - 1])
        window_start += 1
    return result


assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
assert rolling_max([]) == []
assert rolling_max([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]

