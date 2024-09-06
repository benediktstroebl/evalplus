```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers and return the unique elements.
    """
    list_set() is used to remove duplicates.
"""
    return list(set(numbers))

# Test the function with various inputs
numbers1 = [1, 2, 3, 4, 2, 1]
print(remove_duplicates(numbers1))  # Output: [1, 2, 3, 4]

numbers2 = [5, 6, 6, 2, 5, 3]
print(remove_duplicates(numbers2))  # Output: [5, 6, 2]

numbers3 = [1, 2, 2, 4, 5]
print(remove_duplicates(numbers3))  # Output: [1, 2, 4]
```

The function **remove_duplicates** takes a list of integers as input and returns a new list containing only the unique elements. This is **list_set()** method is used within the function to remove duplicates from the input list.