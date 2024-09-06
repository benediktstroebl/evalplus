from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    # empty list - sum should be zero, and product should be 1
    if not numbers:
        return 0, 1

    # create sum and product variables, starting with the first element
    sum, product = numbers[0], numbers[0]

    # use enumerate to keep track of index as we loop
    for index, num in enumerate(numbers[1:]):
        # increment the sum
        sum += num
        # increment the product by the value at the current index
        product *= num
    # return the sum and product
    return sum, product

