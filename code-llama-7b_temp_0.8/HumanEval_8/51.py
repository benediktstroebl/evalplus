from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    return (
        sum(numbers),
        # reassign a variable to make this line more readable
        # and avoid passing the list as an argument to the function
        # which requires unnecessary extra memory
        # and iterating over the list twice
        # this time we pass a variable instead of the list
        # and just pass the list once
        *(
            # using star operator to unpack arguments
            # in this case we pass the sum and the product
            # from the iterated values
            # like a list with two elements
            numbers
            if numbers
            else (0, 1)
        )
    )

