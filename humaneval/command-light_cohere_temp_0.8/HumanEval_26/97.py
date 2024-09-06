```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)


# Test suite
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [5, 5, 5, 6, 6, 6]
result = remove_duplicates(numbers)
print(result)  # Output: [5, 6, 6]
```

This script defines a function `remove_duplicates`, which takes a list of integers as input and returns a new list with duplicates removed. The function works by converting the list to a set to remove duplicates, then converting back to a list. Then, the list is returned.