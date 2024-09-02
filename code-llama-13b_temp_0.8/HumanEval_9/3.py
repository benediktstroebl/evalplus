from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    best = numbers[0]
    max_list = [best]
    for number in numbers[1:]:
        if number > best:
            best = number
        max_list.append(best)
    return max_list

