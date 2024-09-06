from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    best_max = numbers[0]
    result = [best_max]
    for number in numbers[1:]:
        best_max = number if number > best_max else best_max
        result.append(best_max)
    return result

