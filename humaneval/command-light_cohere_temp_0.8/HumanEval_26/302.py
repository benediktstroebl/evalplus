```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize an empty set to store unique integers.
    set_ = set()
    for num in numbers:
        set_.add(num)
    return [num for num in set_ if num not in numbers]

# Test case: Remove duplicates from list [1, 2, 3, 2, 4]
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)

# Test case: Remove duplicates from list [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]
result = remove_duplicates(numbers)
print(result)

# Test case: Remove duplicates from list [1, 2, 3, 4, 3]
numbers = [1, 2, 3, 4, 3]
result = remove_duplicates(numbers)
print(result)
``` 
This Python code defines a function `remove_duplicates` that takes a list of integers as input and removes duplicate elements by utilizing a `set` data structure. The function tests cases to demonstrate its functionality, printing the input list and the resulting list with duplicates removed.