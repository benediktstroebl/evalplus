from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = max(numbers)
    previous_max = current_max
    result = [current_max]

    for i in range(1, len(numbers)):
        if numbers[i] > current_max:
            current_max = numbers[i]
        else:
            result.append(current_max)
            current_max = previous_max

    return result

