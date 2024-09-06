from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = []

    for i in range(len(numbers)):
        # Check if rolling_max list is empty
        if not rolling_max:
            rolling_max.append(numbers[i])
        # Check if numbers[i] is greater than rolling_max[i-1]
        elif numbers[i] > rolling_max[-1]:
            rolling_max.append(numbers[i])
        else:
            rolling_max.append(rolling_max[-1])

    return rolling_max

