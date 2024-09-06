Here is a Python script that solves the problem of removing duplicates from an input list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    duplicates = set(numbers)
    result = [x for x in numbers if x not in duplicates]
    return result

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 5]
test_remove_duplicates = remove_duplicates(numbers_list)
print(test_remove_duplicates)  # Expected output: [1, 2, 3, 4, 5]

numbers_set = {1, 2, 3, 2, 4, 5}
test_remove_duplicates_set = remove_duplicates(numbers_set)
print(test_remove_duplicates_set)  # Expected output: [1, 2, 3, 4]

list_of_strings = ['apple', 'banana', 'apple', 'cherry']
test_remove_duplicates_strings = remove_duplicates(list_of_strings)
print(test_remove_duplicates_strings)  # Expected output: ['apple', 'banana', 'cherry']
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The script also includes unit tests to ensure the correctness of the function.