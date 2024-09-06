```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, _ in sorted((n, n + 1) for n in numbers)]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print("Test case 1: ", rolling_max(numbers))

numbers = [1, 3, 4, 2, 5, 6]
print("Test case 2: ", rolling_max(numbers))

numbers = [1, 2, 2, 3, 4, 5, 6]
print("Test case 3: ", rolling_max(numbers))

numbers = [4, 2, 1]
print("Test case 4: ", rolling_max(numbers))

numbers = [5, 6, 7]
print("Test case 5: ", rolling_max(numbers))

```
This script defines a function `rolling_max` that calculates the rolling maximum element in a list. It utilizes a `sorted` function with a custom lambda function `(n, n+1)` to determine the rolling maximum. The test cases pass the