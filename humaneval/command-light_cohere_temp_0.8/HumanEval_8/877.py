```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases
test_sum_product = [
    [1,],
    [],
    [1, 2, 3],
    [10, 20, 30],
    (40, 8001)
]

for test_num, expect in test_sum_product:
    actual = sum_product(test_num)
    print(f"Test {test_num}: {actual}, Expected: {expect}")
```
The above script defines a function `sum_product` that calculates the sum and product of a list of integers. The test cases are then passed as a list, and the function is tested with each case. 

The test cases cover different scenarios: empty list, list with a single element, list with multiple elements, and a large list. The output will show the expected result for each test case.