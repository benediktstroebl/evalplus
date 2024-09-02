from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window_size = 2
    current_max = max(numbers)
    previous_max = []
    for i in range(1, len(numbers) - window_size):
        window = [numbers[i], numbers[i+1], numbers[i+2]]
        if window[-1] > current_max:
            current_max = window[-1]
        previous_max.append(current_max)
    return previous_max