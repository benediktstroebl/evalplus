from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return 0, 1
    else:
        n = len(numbers)
        result = [0] * n
        result[0] = 1
        for i in range(1, n):
            result[i] = numbers[i-1] * result[i-1]
        return result[n-1], result[0]

