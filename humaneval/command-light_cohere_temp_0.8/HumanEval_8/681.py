```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_cases = [
    [], (0, 1),
    [1, 2, 3], (6, 12),
    [10, 20, 30], (100, 300)
]

results = []

for test_data in test_cases:
    result = sum_product(test_data)
    results.append((test_data, result))

# Print the results
for idx, test_case in enumerate(test_cases):
    print(f"Test case {idx+1}: {test_case} -> {results[idx]}")
```