```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with different inputs
test_cases = [
    [], 0, 1,
    [1, 2, 3], (3, 6)
  ]

for case in test_cases:
    result = sum_product(case)
    print(f"Input: {case}, Expected Output: {result}")
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It returns a test the test cases to verify the correctness of the function, and the test results are printed.