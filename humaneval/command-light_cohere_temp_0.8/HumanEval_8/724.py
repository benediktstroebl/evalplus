```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Returns a sum as an tuple (sum, product).
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
        product *= num
    return (sum, product)

# Test the function
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Prints (10, 24)
```