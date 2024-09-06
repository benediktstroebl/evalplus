from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_in_sequence: List[int] = []
    for element in numbers:
        if not max_in_sequence:
            max_in_sequence.append(element)
        elif max_in_sequence[-1] < element:
            max_in_sequence.append(element)
        else:
            max_in_sequence.append(max_in_sequence[-1])
    return max_in_sequence

