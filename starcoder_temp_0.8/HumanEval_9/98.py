from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    last_seen_maximums = [numbers[0]]

    for i, n in enumerate(numbers):
        if n > last_seen_maximums[-1]:
            last_seen_maximums.append(n)
        else:
            last_seen_maximums.append(last_seen_maximums[-1])

    return last_seen_maximums[1:]

