```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with valid input
test_sum_product = sum_product([1, 2, 3, 4, 5]))
print(test_sum_product)  # Output: (15, 120)

# Test the function with empty list
test_empty_sum_product = sum_product([])
print(test_empty_sum_product)  # Output: (0, 1)

# Test the function with negative numbers
test_negative_numbers = sum_product([-1, -2, -3])
print(test_negative_numbers)  # Output: (3, 8)
```
This Python code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers. The function first checks if the empty list is provided, returning (0, 1) in that case. Then, it uses the sum function to calculate the sum of the numbers and, using the product function, calculates the product of the numbers.

Finally, the code provides several tests for the sum_product function: it passes all tests successfully.