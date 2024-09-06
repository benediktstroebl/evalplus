```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()]
```

# Unit tests
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

# Test for empty list
assert remove_duplicates([]) == []

# Test with list of strings (should treat as integers)
assert remove_duplicates(["a", "b", "c"]) == [1]
```