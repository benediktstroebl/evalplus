```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(enumerate(numbers), reverse=True) if num > numbers[numbers.find(max=numbers)])[0]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 5, "Error: Rolling maximum not found."
assert result == [1, 2, 3, 3, 3], "Error: Rolling maximum not correct."

```