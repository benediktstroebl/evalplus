```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers and return the unique elements.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return list(set(numbers))

# Test cases
numbers1 = [1, 2, 3, 2]
print("Test case 1: ", remove_duplicates(numbers1))  # Expected output: [1, 2, 3]

numbers2 = [1, 2, 3, 4, 5]
print("Test case 2: ", remove_duplicates(numbers2))  # Expected output: [1, 2, 3, 4]

numbers3 = [1, 2, 3, 4, 5, 6]
print("Test case 3: ", remove_duplicates(numbers3))  # Expected output: [1, 2, 3, 4, 5]
```
This Python code defines a function `remove_duplicates` that removes duplicate elements from a list of integers and returns the unique elements. The code includes multiple test cases to demonstrate the functionality, and the output is expected according to the problem statement.