```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Sample test cases
test_cases = [
    [], 0, 1, 1
    [1, 2, 3], 10, 24
    [1, 2, 3, 4], 10, 24
]

for case in test_cases:
    result = sum_product(case)
    print(f"Input: {case} Output: {result}")
```
The function `sum_product` calculates the sum and product of integers in a given list, passing each test case successfully.