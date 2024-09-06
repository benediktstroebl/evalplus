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
        return 0, 1

    # initialize the sum and product
    n = len(numbers)
    s = 0
    p = 1

    # iterate through the list and update the sum and product
    for i in range(n):
        s += numbers[i]
        p *= numbers[i]

    return s, p

