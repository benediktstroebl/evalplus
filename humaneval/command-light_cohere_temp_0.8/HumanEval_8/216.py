```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    result = numbers[0] * numbers[1]
    for num in numbers[1:]:
        result = result + num * numbers[0]
    return (result, result)

# Test cases
test_cases = [
    [0, 1],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [10, 20, 30],
    [1, 2, 3, 4, 5, 6, 7]
]

for test_case in test_cases:
    actual_sum_product, actual_product = sum_product(test_case)
    print(f"Test case: {test_case}, {actual_sum_product}, {actual_product}")
```