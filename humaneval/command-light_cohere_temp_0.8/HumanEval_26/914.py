```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[:]]


# Unit tests
numbers = [1, 2, 3, 2, 4, 2, 3, 5]
test_remove_duplicates = [remove_duplicates(numbers)]
print(test_remove_duplicates)  # expected output: [1, 2, 3, 4, 5]
```