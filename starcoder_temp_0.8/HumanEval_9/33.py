from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        raise ValueError("List must be a non empty sequence.")
    last_max = numbers[0]
    result = [last_max]
    for number in numbers[1:]:
        if last_max < number:
            last_max = number
        result.append(last_max)
    return result
