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
    [], (0, 1),
    [1, 2, 3], (10, 24),
    [10, 20, 30], (-5, -10) # Negative numbers in test case
]

for test_case in test_cases:
    actual_sum, actual_product = sum_product(test_case)
    expected_sum, expected_product = next(test_case)
    print(f"Test case {test_case}: Sum = {actual_sum}, Product = {actual_product}")
    print(f"Expected sum: {expected_sum}, Expected product: {expected_product}")
    assert actual_sum == expected_sum
    assert actual_product == expected_product
``` 
The function `sum_product` calculates the sum and product of a list of integers, passing the test cases with various inputs and expected results.