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
    else:
        res = []
        for i in range(len(numbers) - 1):
            res.append(numbers[i] * numbers[i + 1])
        return sum(numbers) + sum(res), numbers[0] * sum_product(numbers[1:])[1]

