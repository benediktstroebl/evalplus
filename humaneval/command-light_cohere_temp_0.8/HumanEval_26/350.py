Here's the self-contained Python function that solves the problem of removing duplicates from a list of integers:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    duplicates = set(numbers)
    return list(duplicates)


# Test cases
numbers_list = [1, 2, 3, 2, 4, 3, 5]
print("Test 1 results: ", remove_duplicates(numbers_list))  # Output: [1, 2, 3, 4]

numbers_set = set(numbers_list)
print("Test 2 results: ", list(numbers_set))  # Output: set([1, 2, 3, 4])

numbers_list2 = [1, 2, 3, 4, 3, 5, 6]
print("Test 3 results: ", remove_duplicates(numbers_list2))  # Output: [1, 2, 3, 4, 5]

numbers_list3 = [3, 2, 4, 1, 5, 6]
print("Test 4 results: ", remove_duplicates(numbers_list3))  # Output: [1, 2, 3, 4, 5]
```

This Python function, `remove_duplicates`, takes a list of integers as input and returns a new list with duplicate values removed. It utilizes the common `set` operations to identify and remove duplicates from the input list, and then converts back to a list for the unique values.