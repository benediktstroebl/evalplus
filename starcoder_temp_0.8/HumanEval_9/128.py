from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_element = numbers[0]
    max_in_seq = [max_element]
    for i in range(1, len(numbers)):
        if numbers[i] > max_element:
            max_element = numbers[i]
        max_in_seq.append(max_element)
    return max_in_seq
