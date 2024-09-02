from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    result = []
    for num in numbers:
        result.append(num)
        if len(result) == 2:
            break
    if len(result) == 2:
        if len(result[0]) == 0:
            return 0, 1
        else:
            return sum(result[0]), sum(result[1])
    return 0, 0