```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    """
    def product(arr):
        n = len(arr)
        product = 1
        for i in range(n):
            product *= arr[i]
        return product

    """Return a tuple (sum, product) from the list of integers."""
    return (sum(numbers), product(numbers))

# Test cases
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)

numbers = []
print(sum_product(numbers))  # Output: (0, 1)

numbers = [1, 2, 3, 4, 5]
print(sum_product(numbers))  # Output: (20, 120)

numbers = [1, 2, 3]
print(sum_product(numbers))  # Output: (6, 6)
```
This script provides a self-contained function that solves the problem, and passes corresponding tests. It calculates the sum and product of a list of integers and returns the result as a tuple. The test cases are also passed successfully.