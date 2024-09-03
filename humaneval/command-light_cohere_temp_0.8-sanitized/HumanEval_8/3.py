from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of integers in list
    Args:
        numbers: A list of integers
    Returns:
        tuple: sum_product value
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
numbers = [1, 2, 3, 4]