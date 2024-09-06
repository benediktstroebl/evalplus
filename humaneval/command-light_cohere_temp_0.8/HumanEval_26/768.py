```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Tests
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
assert len(result) == 3, "Result does not have expected length"
assert set(result) == set([1, 3, 4]), "Duplicates are not removed"

print("Test passed!")
```