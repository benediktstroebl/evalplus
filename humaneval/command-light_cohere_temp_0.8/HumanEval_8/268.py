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
    [], 0, 1,
    [1, 2, 3, 4], (10, 24)
]

# Function call and tests results
for test_case in test_cases:
    result = sum_product(test_case)
    print("Test case:", test_case)
    print("Result:", result)
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function then passes these tests with a series of test cases, and the results are printed.