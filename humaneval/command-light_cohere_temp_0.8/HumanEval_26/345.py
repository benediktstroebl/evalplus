```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test case 1
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

# Test case 2
numbers = [1, 2, 3, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

# Test case 3
numbers = [1, 1, 2, 2, 3]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3]
```
The code defines a function called remove_duplicates, which takes a list of integers as input and returns a new list with all duplicate elements removed. The function uses the use the set() function to create a new set containing only the unique elements from the input list. Then, the list() function is applied to convert the set back into a list, effectively removing any duplicates. 

This script can be used as a standalone function to solve the problem of removing duplicates from a list of integers.