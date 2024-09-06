```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return [x for x in numbers if x not in set(numbers)]


# Test case
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```