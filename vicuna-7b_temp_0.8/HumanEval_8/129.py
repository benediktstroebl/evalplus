from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Check if the input list is empty
    if not numbers:
        return 0, 1
    
    # Initialize sum and product to 0 and 1 respectively
    sum = 0
    product = 1
    
    # Iterate over the input list
    for num in numbers:
        # Add the current number to the sum
        sum += num
        # Multiply the current number by the product
        product *= num
        
    # Return the sum and product
    return sum, product

