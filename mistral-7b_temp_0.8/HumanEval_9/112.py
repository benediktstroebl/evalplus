from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    window = []
    max_number = -1

    for i, num in enumerate(numbers):
        window.append(num)
        max_number = max(max_number, num)

        while i >= len(numbers) - len(window):
            if window[0] == max_number:
                del window[0]
            else:
                break

    return window

