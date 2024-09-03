from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Returns a tuple consisting of a sum and a product of all the integers in a list.
    Args: 
        numbers (List[int]): A list of integers.
    Returns: tuple(numbers), containing the sum and product of all the integers.
"""
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
numbers = [1, 2, 3, 4]