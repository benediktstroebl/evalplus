from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if len(numbers) == 0:
        return 0, 1
    first, second = numbers[0], numbers[1:]
    sum_, product = sum_product(second)
    return sum_ + first, product * first
