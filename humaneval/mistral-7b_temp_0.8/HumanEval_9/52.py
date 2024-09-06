from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_val = numbers[0]
    max_pos = 0

    for i in range(1, len(numbers)):
        if max_val < numbers[i]:
            max_val = numbers[i]
            max_pos = i

    return [max_val] + [max_val for _ in range(len(numbers) - 1)]
