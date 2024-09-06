from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_product = tuple(map(lambda x: x, numbers))
    for i in range(len(numbers)): 
        sum_product = tuple(map(lambda x, y: x + y, sum_product, numbers))
        product_numbers = tuple(map(lambda x: x, numbers))
        product_numbers = tuple(map(lambda x, y: x * y, product_numbers, numbers))
        
    print(sum_product)
    print(product_numbers)
    return sum_product, product_numbers

