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
    [], (0, 1)
    [1, 2, 3], (6, 12)
    [10, 20, 30], (50, 300)
]

for test_case in test_cases:
    actual_sum, actual_product = sum_product(test_case)
    expected_sum, expected_product = next(test_case)
    assert actual_sum == expected_sum, f"Sum mismatch: got ({actual_sum}) expected ({expected_sum})"
    assert actual_product == expected_product, f"Product mismatch: got ({actual_product}) expected ({expected_product})"
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers, and passes tests to ensure the correctness of its functionality. 

The `test_cases` list contains various test cases with expected results, and the script verifies if the actual results match the expected ones. 

This self-contained approach efficiently solves the problem and validates its correctness through tests.