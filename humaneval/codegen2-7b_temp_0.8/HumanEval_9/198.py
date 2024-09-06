from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_max = numbers[0]
    max_elements = []

    for i in range(1, len(numbers)):
        if numbers[i] > previous_max:
            previous_max = numbers[i]
            max_elements.append(previous_max)
        else:
            max_elements.append(previous_max)

    return max_e
