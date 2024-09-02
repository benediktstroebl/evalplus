from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = []
    for idx in range(len(numbers)):
        if idx == 0:
            max_so_far.append(numbers[idx])
        else:
            if numbers[idx] >= max_so_far[-1]:
                max_so_far.append(numbers[idx])
            else:
                max_so_far.append(max_so_far[-1])

    return max_so_far

