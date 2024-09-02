from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_number = numbers[0]
    max_sequence = [max_number]

    for n in numbers[1:]:
        if max_number < n:
            max_number = n
        max_sequence.append(max_number)

    return max_sequence

