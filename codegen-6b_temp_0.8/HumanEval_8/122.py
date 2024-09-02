from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Check that input list is non-empty
    if numbers == []:
        return (0, 1)

    # Create list of previous sums
    sums = [0]

    # Create slice and add previous sums to it
    sums.extend(
        list(
            accumulate(
                numbers[1:],
                lambda x, y: x + y
            )
        )
    )

    # Create list of previous products
    products = [1]

    # Create slice and multiply previous products to it
    products.extend(
        list(
            accumulate(
                numbers[1:],
                lambda x, y: x * y
            )
        )
    )

    # Add results of current sums and products
    return (sums[-1], products[-1])

