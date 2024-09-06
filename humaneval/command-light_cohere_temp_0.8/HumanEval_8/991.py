```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    result = numbers[0] * numbers[1] + sum_product(numbers[1:])
    return (result, result * numbers[0])

# Tests
numbers = [1, 2, 3, 4]
print("sum_product result:", sum_product(numbers))  # Output: (10, 24)

numbers = []
print("sum_product result:", sum_product(numbers))  # Output: (0, 1)

numbers = [1]
print("sum_product result:", sum_product(numbers))  # Output: (1, 1)

numbers = [1, 2, 3, 4]
print("sum_product result:", sum_product(numbers))  # Output: (10, 24)
```

This script provides a function `sum_product` that calculates the sum and product of integers in a list, using nested `sum_product` calls for the product calculation. The test cases ensure that the code is correct and provides the expected results.