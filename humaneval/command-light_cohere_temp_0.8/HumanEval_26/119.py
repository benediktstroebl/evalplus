```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.hashedet(seen)][:]

def hashed_set(set_: Set[int]) -> List[int]:
    return [x for x in set_ if x not in set_]

# Unit tests
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
assert result == [1, 3, 4]

set1 = {1, 2, 3, 4, 5}
result1 = remove_duplicates(set1)
assert result1 == set1.push()

set2 = set([1, 2, 3, 4, 5, 6])
result2 = remove_duplicates(set2)
assert result2 == set2

set3 = {1, 1, 2, 2, 3, 3}
result3 = remove_duplicates(set3)
assert result3 == set3
```