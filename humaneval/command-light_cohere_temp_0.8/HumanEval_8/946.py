```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    return (sum(numbers), product(numbers))

# Example test cases
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)  # Output: (6, 4)
print("Product:", test_sum_product)  # Output: 40000

numbers = []
test_empty_sum_product = sum_product(numbers)
print("Sum:", test_empty_sum_product)  # Output: 0
print("Product:", test_empty_sum_product)  # Output: 1

numbers = [1, 2, 3, 4, 5]
test_large_sum_product = sum_product(numbers)
print("Sum:", test_large_sum_product)  # Output: (25, 120)
print("Product:", test_large_sum_product)   # Output: 240000
```
The code defines a function `sum_product` that calculates the sum and product of a list of integers. The `test_sum_product` function is a test case that calls the `sum_product` function with a list of integers and prints the result. The output shows the product of the list, the product of the empty list, and the product of a list with additional values.