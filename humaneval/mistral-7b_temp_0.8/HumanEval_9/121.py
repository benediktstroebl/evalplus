from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Adding start with an empty list to the loop, because
    # We are getting the first value in the last iteration
    max_values = []
    for n in numbers:
        if not max_values:
            max_values.append(n)
        else:
            max_values.append(max(max_values[-1], n))
    return max_values

