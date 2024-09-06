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
    [],  # Empty list, expected (0, 1)
    [1, 2, 3],  # List with 3 integers, expected (3, 12)
    [1, 2, 3, 4],  # List with 4 integers, expected (10, 24)
]

# Test results
print("Sum product results:")
for test_case in test_sum_product:
    actual = sum_product(test_case)
    print((f"Case {test_case}: {actual}, expected {test_case[1]:format(test_case[1])}))
```