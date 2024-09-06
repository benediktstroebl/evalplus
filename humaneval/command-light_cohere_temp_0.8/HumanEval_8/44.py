```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
test_cases = [
    [], 0, 1,
    [1, 2, 3], (3, 6)
  ]

for test_case in test_cases:
    actual_sum, actual_product = sum_product(test_case)
    print(f"Expected ({test_case}), got ({actual_sum}, {actual_product})")
```
This Python code defines a function called sum_product that calculates the sum and product of a list of integers. The function iterates through a list and maintains two variables: product and sum, respectively.

The code also has a list of test cases, where the function is called with a list of integers. Each test case is run through and the actual result is printed out, along with the expected result.