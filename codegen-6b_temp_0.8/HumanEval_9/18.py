from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # the idea is to use the fact that each element is increasing to the right,
    # so we keep a maximum value until the current element, and compare it to
    # the current maximum
    max_so_far = numbers[0]
    output = []
    for value in numbers:
        if max_so_far < value:
            max_so_far = value
        output.append(max_so_far)
    return output

