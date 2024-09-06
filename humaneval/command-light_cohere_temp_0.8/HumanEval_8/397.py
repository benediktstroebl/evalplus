```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
test_cases = [
    [], 0, 1
    [1, 2, 3], (6, 12)
    [1, 2, 3, 4], (10, 24)
]

results = []

for test_case in test_cases:
    result = sum_product(test_case)
    results.append(result)

print("Test cases:", results)
```