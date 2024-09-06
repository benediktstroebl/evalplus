```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return list(numbers)

# Test cases
numbers_list = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers_list)
assert result == [1, 3, 4, 5]

numbers_set = {1, 2, 3, 4, 5}
result = remove_duplicates(numbers_set)
assert result == set({1, 3, 4, 5})

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected
```