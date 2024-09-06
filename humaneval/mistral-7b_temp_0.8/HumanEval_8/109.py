from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Empty list case
    if not numbers:
        return 0, 1
    # If list not empty
    else:
        # To store sum
        sum = 0
        # To store product
        product = 1
        # Loop over the given list
        for n in numbers:
            # Add each element to sum
            sum += n
            # Multiply with each element
            product *= n
        # Return a tuple containing sum and product
        return sum, product

