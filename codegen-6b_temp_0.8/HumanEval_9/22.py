from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    seq = []
    current_max = numbers[0]
    for i, current in enumerate(numbers):
        if i == 0:
            seq.append(numbers[i])
        else:
            seq.append(max(current_max, current))
            if current > current_max:
                current_max = current
    return seq

