from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    def sum_product_helper(numbers: List[int], partial_sum: int, partial_product: int) -> Tuple[int, int]:
        if not numbers:
            return (partial_sum, partial_product)
        return sum_product_helper(numbers[1:], partial_sum + numbers[0], partial_product * numbers[0])

    return sum_product_helper(numbers, 0, 1)
