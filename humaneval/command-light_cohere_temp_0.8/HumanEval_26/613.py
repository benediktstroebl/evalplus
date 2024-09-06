```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Set to remove duplicates
    return list(numbers)


# Test cases
numbers = [1, 2, 3, 2, 4, 3, 1, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 3, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]
```

This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function works by converting the list into a set to remove duplicates, and then converting back to a list to get the desired result.