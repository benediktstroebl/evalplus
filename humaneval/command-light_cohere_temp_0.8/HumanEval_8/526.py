```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Args:
    numbers (List[int]): A list of integers.
    Returns: A tuple containing the sum and product of all integers in the list.
    """
    empty sum should be equal to 0 and empty product should be equal to 1.
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with sample input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This code defines a sum_product function that takes a list of integers as input and returns a tuple containing the sum and product of the integers. It then iterates through theums to calculate the sum and product, and finally, returns the result.