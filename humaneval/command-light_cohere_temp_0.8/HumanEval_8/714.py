```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in the list.
    Args: 
    numbers: list of integers
    Returns: tuple of (sum of the numbers, product of the numbers)
    """
    product = 1
    sum = 0 
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```