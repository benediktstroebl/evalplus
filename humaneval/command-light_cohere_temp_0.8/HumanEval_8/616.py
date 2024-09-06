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
test_cases = [
    [], 0, 1,
    [1, 2, 3, 4], (10, 24)
]

for case in test_cases:
    result = sum_product(case)
    print(f"Case {case}: {result}")
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function is then passed a list of test cases, and prints the results for each test.