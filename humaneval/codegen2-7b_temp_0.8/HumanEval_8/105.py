from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    try:
        total = sum(numbers)
        product = 1
        for i in numbers:
            product *= i
    except TypeError as err:
        raise TypeError("Passed input is not a list.") from err
    return (total, product)

