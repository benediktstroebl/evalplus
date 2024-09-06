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
    [], 0, 1,
    [1, 2, 3], (3, 6)
  ]

for test_case in test_cases:
    result = sum_product(test_case)
    print(f"Test case: {test_case}, {result}")
```
The script defines a function called `sum_product` that calculates the sum and product of a list of integers. The `test_cases` variable is a list of test cases, each consisting of a list of integers and the expected result. The script then iterates through each test case, calculates the result using the `sum_product` function, and prints the test case and the result.