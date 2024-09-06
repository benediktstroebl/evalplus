from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    current_max = numbers[0]
    rolling_max = []
    for num in numbers:
        if num > current_max:
            rolling_max.append(num)
            current_max = num
        else:
            rolling_max.append(current_max)
    return rolling_max

