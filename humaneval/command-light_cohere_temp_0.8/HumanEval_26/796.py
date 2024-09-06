```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 2, 3, 5]
result = remove_duplicates(numbers_list)
should_be = [1, 2, 3, 4, 5]
assert len(result) == 5, f"Result should be {5}, but got {len(result)}"
assert list(set(numbers_list)) == set(should_be), f"Elements should be unique, but they're not: {set(numbers_list)} != {set(should_be)}"
print(result)
```