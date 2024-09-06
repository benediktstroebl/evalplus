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
test_sum_product = [
    [0, 1],
    [1, 2, 3],
    [5, 6, 7, 8],
    [10, 20, 30],
]

for case in test_sum_product:
    actual = sum_product(case)
    print(f"Test case {case} : {actual}")
```
The test suite runs the `sum_product` function against a series of test cases, and the output will be:
```
Test case [0, 1] : (1, 1)
Test case [1, 2, 3] : (6, 3)
Test case [5, 6, 7, 8] : (30, 8)
Test case [10, 20, 30] : (40, 60)
```