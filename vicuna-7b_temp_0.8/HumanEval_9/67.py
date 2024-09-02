from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    total_max = 0
    rolling_max = []
    current_max = max(numbers)
    for i in range(len(numbers)):
        if numbers[i] == current_max:
            rolling_max.append(current_max)
            current_max = max(numbers)
        else:
            if current_max > total_max:
                rolling_max.append(total_max)
                total_max = current_max
            rolling_max.append(current_max)
            current_max = numbers[i]
    return rolling_max

