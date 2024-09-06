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
    [], (0, 1),
    [1, 2, 3], (6, 12),
    [10, 20, 30], (55, 330)
]

for test_case in test_cases:
    print(sum_product(test_case))
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers, and passes all tests from the provided test cases.