Here is a self-contained Python script that solves the problem of removing duplicates from a list of integers:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    duplicates = set(numbers)
    result = [num for num in numbers if num not in duplicates]
    return result


# Test cases
numbers1 = [1, 2, 3, 2]
print("Test 1 result:", remove_duplicates(numbers1))

numbers2 = [1, 1, 2, 3]
print("Test 2 result:", remove_duplicates(numbers2))

numbers3 = [1, 4, 5, 6]
print("Test 3 result:", remove_duplicates(numbers3))
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list that contains only the unique integers. The function uses the duplicate detection through the set, which automatically removes duplicates, and then creates a new list with the remaining unique elements.

This code is self-contained and can be used to solve the problem of removing duplicates from any list of integers.