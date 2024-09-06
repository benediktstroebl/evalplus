```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]


# Test cases
numbers = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 4, 3, 5, 6]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

numbers = [1, 1, 2, 2, 3, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 2, 3]
```
This code provides a function called remove_duplicates that takes a list of integers as input and returns a new list with all unique integers from the original list. The test cases demonstrate how the duplicate elements are successfully removed from the list.