from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window_size = 5
    current_max = numbers[0]
    current_window = [current_max]
    for i in range(1, len(numbers)):
        if i < window_size:
            current_window.append(numbers[i])
        else:
            if numbers[i] > current_max:
                current_max = numbers[i]
            current_window.append(numbers[i])
    return current_window

