from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 10  # the number of values to look at
    window = 5  # the number of values to consider from the current window
    current_max = numbers[0]

    for i in range(1, len(numbers)):
        for j in range(window):
            if numbers[i] >= current_max:
                current_max = numbers[i]
        window -= 1

    return [current_max] * n + [None] * (window - len(numbers) + 1)

