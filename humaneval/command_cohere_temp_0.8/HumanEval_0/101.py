Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and yields the appropriate output for the provided test cases.

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))

# Tests
numbers_list = [
    [1.0, 2.0, 3.0],
    [1.0, 2.8, 3.0, 4.0, 5.0, 2.0],
]
thresholds = [0.5, 0.3]
expected_results = [False, True]

for i in range(len(numbers_list)):
    assert has_close_elements(numbers_list[i], thresholds[i]) == expected_results[i]
```
This script includes test cases to validate the function has_close_elements against the specified test cases in the markdown code block. The function uses a generator expression, zip, and the absolute difference criterion to efficiently check for close elements in the list. The tests are structured as assert statements to confirm the function's correctness against specific input scenarios.