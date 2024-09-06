```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in set(numbers) if num not in numbers]


# Test the remove_duplicates function
numbers = [1, 2, 3, 2, 4, 3, 1, 5]
result = remove_duplicates(numbers)
print(result)

# Test removing non-numeric elements
numbers = [".a", 2, 3, 4]
result = remove_duplicates(numbers)
print(result)
```