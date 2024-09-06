```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(sorted(numbers), numbers) if i < numbers[-1]]

# Test the function with a sample input
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```