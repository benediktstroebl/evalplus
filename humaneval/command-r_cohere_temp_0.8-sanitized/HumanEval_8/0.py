from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in the list.
    If the list is empty, the sum should be 0 and the product should be 1.
    
    Parameters:
        numbers (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing sum and product of the list elements.
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)