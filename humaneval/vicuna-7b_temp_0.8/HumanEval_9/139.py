from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_values = [max(numbers)]
    for n in range(1, len(numbers)):
        current_max = max(numbers[:n])
        max_values.append(current_max)
        numbers = [n] + numbers[n:]
    return max_values[-1]

