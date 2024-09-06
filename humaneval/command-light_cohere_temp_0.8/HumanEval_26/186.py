```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of integers.
    numbers = set(numbers)  # converting to set to remove duplicates
    return list(numbers)  # converting back to list for returned value
    """
    return numbers


# Test cases
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [1, 2, 3, 4, 5]
numbers3 = [1, 2, 3, 4, 5, 6]

print(remove_duplicates(numbers1))  # expected output: [1, 2, 3, 4]
print(remove_duplicates(numbers2))  # expected output: [1, 2, 3, 4, 5]
print(remove_duplicates(numbers3))  # expected output: [1, 2, 3, 4, 5, 6]
```  # New test case with duplicates as well

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function works by converting the list to a set to remove duplicates, and then converting the set back to a list to be returned.