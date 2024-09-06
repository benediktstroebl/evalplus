```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of integers.
    Args: 
        numbers: list of integers
    Returns: 
        tuple: (sum, product) where sum is the sum of the numbers and product is the product of the numbers
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
``` 
This code defines a function sum_product that takes a list of integers as an argument and returns a tuple of two integers. It then iterates through numbers in the list, calculating the sum and product of the integers. The function then returns a tuple of the sum and product of the numbers in the list.