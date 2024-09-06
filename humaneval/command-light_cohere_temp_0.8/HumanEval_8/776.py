```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list
        return (0, 1)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Test cases
test_cases = [
    [], (0, 1)
    [1, 2, 3], (6, 6)
    [10], (6, 1000)
]

for test_case in test_cases:
    result = sum_product(test_case)
    print(f"Input: {test_case} Output: ({result[0], result[1]})")
```
This Python code defines a function called sum_product that calculates the sum and product of a list of integers. It also includes a test cases that cover the possible scenarios of an empty list, a list of positive numbers, and a list of numbers multiplied by 10. The code then iterates over each test case, calling the sum_product function and printing out the input and output pairs.