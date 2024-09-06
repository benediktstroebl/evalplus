```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with various inputs
test_cases = [
    [], 0, 1,
    [1, 2, 3], (6, 12),
    [10], (55, 110),
]

for case in test_cases:
    result = sum_product(case)
    print(f"Input: {case} Result: {result}")
```
This script defines a function sum_product that calculates the sum and product of a list of integers. It then tests the scenario where the test the function with different inputs. The test cases include empty lists, single numbers, pairs of numbers, and larger arrays of numbers. The result of each test case is then printed.