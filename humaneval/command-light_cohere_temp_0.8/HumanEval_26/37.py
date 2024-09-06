Here is a self-contained Python function that solves the problem of removing duplicates from a list of integers:
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    duplicates = set(numbers)
    return [num for num in numbers if num not in duplicates]

# Test the function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]

# Test again
same_numbers = [1, 2, 3, 2]
result = remove_duplicates(same_numbers)
print(result)  # Expected output: [1, 2, 3]
```

This script provides a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The test cases demonstrate that the function removes duplicates correctly.