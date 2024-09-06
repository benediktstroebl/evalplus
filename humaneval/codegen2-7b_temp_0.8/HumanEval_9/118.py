from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_sum = 0
    max_sequence = []
    for number in numbers:
        max_sum = max(max_sum, number)
        if max_sum < number:
            max_sequence.append(max_sum)
    return max_sequence

