```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x == max(numbers, default=0)]

# Test case:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

# Test case 2:
from collections import Counter
numbers = [1, 2, 2, 3, 3, 4, 2, 3, 3]
result = rolling_max(numbers)
print(result)
```
This code provides a self-contained function `rolling_max` that generates a list of the rolling maximum elements from a given list of integers. It uses a test to pass the test cases and print the results.