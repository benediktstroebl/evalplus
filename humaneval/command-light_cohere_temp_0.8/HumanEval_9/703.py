```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, n in zip(numbers, numbers) if n > x or not numbers[n]]

# Test the function with simple inputs
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7, "Error: Rolling max function returned an incorrect list length"
assert all(result == [1, 2, 3, 3, 3, 4, 4])
```