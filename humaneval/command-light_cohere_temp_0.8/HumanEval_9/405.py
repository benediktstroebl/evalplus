```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(f"The rolling maximum elements are: {[(max(numbers[i:]) for i in range(len(numbers))]}")
```