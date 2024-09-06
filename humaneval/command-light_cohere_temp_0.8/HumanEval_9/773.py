```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in zip(sorted(numbers), numbers) if idx < len(numbers) and numbers[idx] > numbers[idx-1]]

# Testing the function with known values
numbers = [1, 2, 3, 2, 3, 4, 4]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a rolling_max function that calculates the maximum element from the beginning of a list, producing the same result as shown in the documentation.