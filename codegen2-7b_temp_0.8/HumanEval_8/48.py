from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    try:
        sum_, product_ = 0, 1
        for i in numbers:
            sum_ += i
            product_ *= i
        return sum_, product_
    except ValueError:
        return (0, 1)

