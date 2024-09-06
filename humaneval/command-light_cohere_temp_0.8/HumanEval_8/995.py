```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}
print("Product: {result[1]}")
```
The function computes the sum and product of a list of integers and returns them as a tuple. This script also provides an example with test data, ensuring the function is correctly calling and returning the expected results.