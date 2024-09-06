```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_cases = [
    [],  # Empty list
    [1, 2, 3],  # Elements list with sum and product
    [1, 2, 3, 4],  # Multiple elements list with sum and product
]

for test_case in test_cases:
    actual_sum, actual_product = sum_product(test_case)
    print(f"Test {test_case} sum: {actual_sum}, product: {actual_product}")
```
The code defines a function sum_product that calculates the sum and product of a list of integers. It uses the particular list as an parameter and returns a tuple with the sum and product of the numbers. The function is then passed to a test case, which contains different lists to test its functionality. 

The test case prints the result of the function with each test case and verifies if the output matches the expected sum and product of the numbers.