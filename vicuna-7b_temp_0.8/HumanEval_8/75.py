from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # check if the list is empty
    if not numbers:
        # return empty sum and product
        return 0, 1

    # if the list is not empty, compute the sum and product
    sum = 0
    product = 1

    for num in numbers:
        # add the current number to the sum and multiply the product by the current number
        sum += num
        product *= num

    # return the sum and product
    return sum, product

