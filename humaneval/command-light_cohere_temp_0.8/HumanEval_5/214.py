```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter] * 2)]

# Test cases
test_data = [
    [], 4, 
    [1, 2, 3], 4, 
    [10, 20, 30], 40, 
]

test_cases = [True, False] * zip(test_data, test_cases)

for test_values, test_should_pass in test_cases:
    actual_result = intersperse(test_values, 4)
    if actual_result != test_values:
        print(f"Test {test_should_pass} failed: {actual_result}, expected: {test_values}")
    else:
        print(f"Test {test_should_pass} passed: {actual_result}")
```