from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    # 1. Find a sum of all elements
    # 2. Find a product of all elements

    # 1. Find a sum of all elements
    sum_all_elements = 0
    for element in numbers:
        sum_all_elements += element

    # 2. Find a product of all elements
    product_all_elements = 1
    for element in numbers:
        product_all_elements *= element

    return (sum_all_elements, product_all_elements)
