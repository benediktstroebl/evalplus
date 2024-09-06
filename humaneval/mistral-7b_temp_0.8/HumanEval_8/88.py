from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    sum_list = [0] * len(numbers)
    product_list = [1] * len(numbers)
    for i, number in enumerate(numbers):
        sum_list[i] = sum_list[i-1] + number
        product_list[i] = product_list[i-1] * number

    return sum_list[-1], product_list[-1]
