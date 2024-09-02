from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window_size = 1
    last_max = numbers[0]
    current_max = last_max

    for number in numbers:
        if number > current_max:
            window_size += 1
            current_max = number
        elif window_size >= len(numbers) - 1:
            window_size -= 1
            if window_size == 0:
                break
            current_max = last_max
        last_max = current_max

    return [current_max]

