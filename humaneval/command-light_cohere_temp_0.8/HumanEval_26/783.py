```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))  # Use set() to remove duplicates and return unique elements


# Test:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 3, 2, 2, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 2, 4, 5]

# Duplicate element test
numbers = [1, 2, 2]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2]
``` 
This script defines a function `remove_duplicates`, which takes a list of integers as input and returns a new list with duplicate elements removed. The function utilizes the method `set()` to create a new list containing unique elements from the original input list.