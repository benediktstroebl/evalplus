from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    res = []
    for i, n in enumerate(numbers):
        current = numbers[i]
        for next_n in numbers[i + 1:]:
            if next_n > current:
                current = next_n
        res.append(current)
    return res

