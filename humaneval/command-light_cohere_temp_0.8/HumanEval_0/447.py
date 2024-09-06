Here is a Python script that contains a self-contained function that solves the problem:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Implementation
    if len(numbers) < 2:
        return False
    if len(numbers) == 2:
        return numbers[0] + numbers[1] <= threshold
    numbers = sorted(numbers)
    for i in range(1, len(numbers) - 1):
        if numbers[i] - numbers[i - 1] <= threshold:
            return True
    return False


# Test case
numbers = [1.0, 2.0, 3.0, 0.0, 5.0, 2.0, 6.0, 7.0]
if has_close_elements(numbers, 0.0.4):
    true