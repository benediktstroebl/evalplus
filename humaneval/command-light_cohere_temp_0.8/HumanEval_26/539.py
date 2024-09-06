```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]


# Test case:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
``` 
This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The `set` is used to create a set of unique integers from the input list.