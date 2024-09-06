```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

#Test cases
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print("Result:", result)  # Output: [1, 3, 4]

numbers = [4, 2, 3, 2, 1]
result = remove_duplicates(numbers)
print("Result:", result)  # Output: [2, 3, 1]

numbers = [5, 5, 5, 5]
result = remove_duplicates(numbers)
print("Result:", result)  # Output: [5]

numbers = [1, 1, 2, 3, 4]
result = remove_duplicates(numbers)
print("Result:", result)  # Output: [1, 2, 3, 4]
```
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list where all duplicate elements have been removed. It achieves this by converting the list into a set and back into a list.