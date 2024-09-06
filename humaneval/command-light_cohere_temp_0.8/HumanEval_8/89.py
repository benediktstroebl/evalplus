```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in the list.
    Parameters: 
    - numbers (List[int]) -> The list of integers
    Returns: 
    - tuple (sum: int, product: int)
    """
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: {result[1]}")
```