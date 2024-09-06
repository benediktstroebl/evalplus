```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculate the sum and product of a list of integers.
    """ 
    return (sum(numbers), product(numbers))
    """
    return (sum(numbers), product(numbers))

# Test the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (6, 24)
print("Product:", result[1])  # Output: 24
```