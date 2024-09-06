```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test the function with a sample input
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all unique integers from the input. The `set()` method is used to remove duplicate elements from the input list.