from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # sum_all = 0
    # product_all = 1
    # for num in numbers:
    #     sum_all += num
    #     product_all *= num
    # return sum_all, product_all
    return (sum(numbers) or 0, (reduce(lambda x, y: x * y, numbers) or 1))

