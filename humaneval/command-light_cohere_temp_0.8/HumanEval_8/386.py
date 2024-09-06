```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple with sum and product of all integers in the list.
    Args:
    numbers: list of integers
    Returns: 
    tuple: (sum, product) 
    """
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)
# Test the function
numbers = [1,2,3,4]
print(sum_product(numbers))
``` 
This Python function, sum_product, is designed to calculate the sum and product of a list of integers. It uses a `typing` to provide better type hints and prevent potential type-related bugs. The function takes a `List[int]` as input and returns a tuple with the sum and product of all integers in the list. It uses a essential loop to calculate the product by multiplying each integer in the list. The function also uses the `sum()` function from the built-in library `collections` to calculate the sum of the integers in the list.