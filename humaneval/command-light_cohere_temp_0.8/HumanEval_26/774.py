Here is a Python script that contains a self-contained function called `remove_duplicates` that solves the problem of removing duplicate values from a list of integers:
```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize a set to store unique values
    unique_values = set(numbers)
    # Create a new list with elements from the set
    result = [value for value in unique_values]
    return result

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 1]
test_result = remove_duplicates(numbers_list)
print("Test 1 Result:", test_result)

numbers_list2 = [1, 2, 2, 4, 3, 5]
test_result2 = remove_duplicates(numbers_list2)
print("Test 2 Result:", test_result2)
```

This script defines a function `remove_duplicates` that takes a list of integers as an argument and creates a set of unique integers from the input list. It then converts this list back into a new list containing only the unique values. The unit tests demonstrate the different test cases for the `remove_duplicates` function.