from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    if not numbers:
        return result

    current_max, remember_max = numbers[0], numbers[0]
    for number in numbers[1:]:
        if number > current_max:
            current_max = number
        else:
            result.append(remember_max)
            remember_max = current_max

    result.append(remember_max)

    return result

