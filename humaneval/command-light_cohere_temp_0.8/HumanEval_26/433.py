```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 0 and num not in seen]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers_list)
should_be = [1, 3, 4]
assert result == should_be

numbers_set = {1, 2, 3, 4, 5}
result = remove_duplicates(numbers_set)
should_be = []
assert result == should_be

```