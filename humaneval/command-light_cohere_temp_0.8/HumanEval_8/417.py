```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases for the function
numbers_test = [1, 2, 3, 4]
result_test = sum_product(numbers_test)
print(f"Test case 1: {result_test}")

numbers_empty = []
result_empty = sum_product(numbers_empty)
print(f"Test case 2: {result_empty}")

numbers_large = [123, 456, 789, 0]
result_large = sum_product(numbers_large)
print(f"Test case 3: {result_large}")
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It utilizes a testing with various cases, passing the test suite successfully.