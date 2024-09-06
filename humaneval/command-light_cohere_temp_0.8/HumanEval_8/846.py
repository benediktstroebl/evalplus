```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Compute the sum and product of a list of integers.
    Args: 
    - numbers: List[int] list of integers. 
    Returns: a tuple consisting of a sum and a product of all the integers in a list
    Return Values: 
    - tuple: (sum, product) 
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```