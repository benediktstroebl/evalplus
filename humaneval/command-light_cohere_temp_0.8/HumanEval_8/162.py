```python
from typing import List

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
    [10, 20, 30], (100, 600)
]

for test_case in test_cases:
    result = sum_product(test_case)
    print(f"Test case: {test_case} => {result})
```

The output of this code will display the test cases and the calculated sum and product for each test case.