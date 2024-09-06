from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    sum_product_list = []
    for n in numbers:
        sum_product_list.append(n)
        sum_product_list.append(n * n)

    sum = 0
    product = 1
    for x in sum_product_list:
        sum += x
        product *= x

    return sum, product

