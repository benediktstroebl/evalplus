```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # remove duplicates from the list
    return list(set(numbers))  # use set to get distinct elements, then convert back to list


# test suite
numbers = [1, 2, 3, 2, 4, 2, 1, 5]
print("Test 1: ", remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 2, 4, 2]
print("Test 2: ", remove_duplicates(numbers))  # expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5, 6]
print("Test 3: ", remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5]
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The test suite includes three tests that demonstrate the functionality of the function.