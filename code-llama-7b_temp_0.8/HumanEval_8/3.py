from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # return tuple(sum(numbers), product(numbers))
    sum_res = 0
    prod_res = 1
    for i in range(len(numbers)):
        sum_res += numbers[i]
        prod_res *= numbers[i]
    return sum_res, prod_res

