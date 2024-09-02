from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers: List[int] = []
    max_so_far: int = numbers[0]
    max_numbers.append(max_so_far)

    for number in numbers[1:]:
        max_so_far = max(number, max_so_far)
        max_numbers.append(max_so_far)

    return max_numbers

