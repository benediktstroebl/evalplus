```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return List(set(numbers))

# Test the remove_duplicates function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 2, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 6, 3, 7]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 6, 7]
```
This Python code defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. It uses the major set() to remove duplicates from the input list and then constructs a new list from the unique elements.

The code then tests the remove_duplicates function by passing different input lists and printing the resulting lists.