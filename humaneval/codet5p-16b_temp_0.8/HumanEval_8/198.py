from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    if not numbers:
        return (0, 1)
    else:
        if len(numbers) == 1:
            return (numbers[0], 1)
        else:
            s, p = sum_product(numbers[:-1])
            return (s + numbers[-1], p * numbers[-1])

