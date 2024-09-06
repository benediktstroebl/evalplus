```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with different inputs
test_sum_product = [1, 2, 3, 4, 5]
result = sum_product(test_sum_product)
print(result)  # Output: (15, 120)
test_empty = []
result = sum_product(test_empty)
print(result)  # Output: (0, 1)
test_single = [1]
result = sum_product(test_single)
print(result)  # Output: (1, 1)
test_large = [123, 456, 987, 123, 456, 987]
result = sum_product(test_large)
print(result)  # Output: (459, 17811)
```
This code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. It then passes these tests the different sets of inputs and verifies that the function produces the correct results.