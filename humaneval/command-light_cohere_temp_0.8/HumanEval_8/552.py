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
    [], 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20],
    [1, 2, 3, 4, 5], 10, 24, 50, 100, 125],
    [20], 0, 1, 2, 4, 8, 16, 32, 64, 128],
    [range(1, 201)], 0, 201, 100000000, 200000000, 30000000]

for test_case in test_cases:
    result = sum_product(test_case)
    print(f"Input: {test_case}, Output: {result}")
```
This Python script defines a function called sum_product that calculates the sum and product of a list of integers. It also provides a specific test cases to validate the function, and prints the test results.