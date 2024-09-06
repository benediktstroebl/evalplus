from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Check for empty list
    if not numbers:
        return 0, 1

    # Initialize the sum and product with respect to the empty list
    sum_empty = 0
    product_empty = 1

    # Check for negative numbers and raise ValueError if any
    for num in numbers:
        if num < 0:
            raise ValueError(f"{num} is not a valid input")

    # Loop through the list and sum up all the numbers
    sum_list = 0
    for num in numbers:
        sum_list += num

    # Return the sum and product
    return sum_list, product_empty * numbers

