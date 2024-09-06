```python
from typing import List, Tuple
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
    [1, 2, 3], (6, 12)
  ]

for test_case in test_cases:
    result = sum_product(test_case)
    print(f"Test case: {test_case}, {result}")
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a `typing` to ensure type compatibility of the input arguments and return values. 

The function is then tested with various input lists using a loop that passes each test case. The results are then printed for each test case, providing a comprehensive evaluation of the function.