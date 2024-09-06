Here's a self-contained Python script that provides a function sum_product, along with test cases:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Test case for an empty list
        return (0, 1)

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_cases = [
    [], (0, 1)  # Empty list
    [1, 2, 3], (6, 12)  # List with numbers
    [10, 20, 30], (50, 300)  # List with large numbers
]

results = []

for case in test_cases:
    result = sum_product(case)
    results.append(result)

print(results)
```

This script defines the function `sum_product`, which returns the sum and product of a list of integers. It also provides test cases to test the function, and the results are printed to the console.