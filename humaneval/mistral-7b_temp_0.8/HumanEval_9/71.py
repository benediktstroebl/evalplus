from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_seq: List[int] = []

    if len(numbers) == 0:
        return max_seq

    for num in numbers:
        if len(max_seq) == 0:
            max_seq.append(num)
        elif max_seq[-1] < num:
            max_seq.append(num)
        else:
            max_seq.append(max_seq[-1])

    return max_seq

