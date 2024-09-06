```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[:seen.seen new_set() &
    new_set() = seen.from_iter(numbers)
    seen |= new_set()
numbers = [1, 2, 3, 2, 4, 3, 1, 4, 2]
result = remove_duplicates(numbers)
print(result)
```