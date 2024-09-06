from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    sequence: List[int] = []
    for i, num in enumerate(numbers):
        if i == 0:
            sequence.append(num)
        else:
            if num > sequence[-1]:
                sequence.append(num)
            else:
                sequence.append(sequence[-1])
    return sequence

