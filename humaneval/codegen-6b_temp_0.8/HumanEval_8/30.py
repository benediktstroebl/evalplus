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
        return (0, 1)
    
    else:
        sum_of_numbers = 0
        for element in numbers:
            sum_of_numbers += element
        
        product_of_numbers = 1
        for element in numbers:
            product_of_numbers *= element
        
        return (sum_of_numbers, product_of_numbers)

