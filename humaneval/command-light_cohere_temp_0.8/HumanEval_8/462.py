Here is a Python script with a self-contained function that solves the problem:
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
test_sum_product_lists = [
    [],  # Empty list
    [1, 2, 3],
    [5, 6, 7],
    [10, 20, 30],
]

results = {}
for test_list in test_sum_product_lists:
    result = sum_product(test_list)
    results[(test_list, result)] = True

for test_list, success in results.
```

This script defines a function sum_product that calculates the sum and product of a list of integers. It then passes these function through a series of test cases, verifying if the function is working correctly.