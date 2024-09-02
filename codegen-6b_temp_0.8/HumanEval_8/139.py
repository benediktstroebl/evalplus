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
        result_sum = 0
        if numbers:
            result_sum = sum(numbers)
        result_product = 1
        if numbers:
            result_product = reduce(lambda x, y: x * y, numbers)
        return result_sum, result_product
    except TypeError:
        return 0, 1

