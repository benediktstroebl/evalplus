```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.is_duplicates(seen, numbers)]


numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
```