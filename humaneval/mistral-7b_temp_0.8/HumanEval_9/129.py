from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Using a list comprehension
    return [max(numbers[:i + 1]) for i in range(len(numbers))]

    # Using a list comprehension with enumerate
    # return [numbers[i] for i in range(len(numbers))]

    # Using a list comprehension and a generator
    # return [i for i in range(len(numbers)) if i > 0]

