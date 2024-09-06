from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far: int = numbers[0]
    max_till_now: int = numbers[0]
    result: List[int] = []

    for number in numbers:
        if number > max_so_far:
            max_so_far = number
        max_till_now = max(max_so_far, max_till_now)
        result.append(max_till_now)

    return result

