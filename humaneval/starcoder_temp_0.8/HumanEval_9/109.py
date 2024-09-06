from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) < 1:
        return []

    max_until_now: int = numbers[0]
    maxes: List[int] = [max_until_now]
    for n in numbers[1:]:
        if n > max_until_now:
            max_until_now = n
        maxes.append(max_until_now)

    return maxes

