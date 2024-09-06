```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers1 = [1, 2, 3]
numbers2 = []
result1 = sum_product(numbers1)
result2 = sum_product([])()
print(f"Test case 1: Result = {result1}")
print(f"Test case 2: Result = {result2}")
```
This code defines a function sum_product that calculates the sum and product of a list of integers. It uses a generic function type parameters, which are promoted to work with Python's type hints. The test cases demonstrate the the results are printed for both test cases.