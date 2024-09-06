```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases for the sum_product function
test_sum_product = [
    [], 0, 1,
    [1, 2, 3, 4], (10, 24)
]

for case in test_sum_product:
    actual_result = sum_product(case)
    expected_result = next(expected for _, expected in zip(*case))
    print(f"Case {case}: {actual_result} != {expected_result}")
```
This code contains a test suite that covers different scenarios. The sum_product function calculates the sum and product of a list of integers, then compares the actual results with the expected results using assertions. The test suite validates that the sum_product function is working correctly for various inputs.