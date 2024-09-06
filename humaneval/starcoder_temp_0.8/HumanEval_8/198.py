from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    def _rec(numbers, acc_sum, acc_product):
        if len(numbers) == 0:
            return (acc_sum, acc_product)
        else:
            return _rec(numbers[1:], acc_sum + numbers[0], acc_product * numbers[0])

    return _rec(numbers, 0, 1)
