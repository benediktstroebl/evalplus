```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num < numbers.count(num)]


# Test cases for the remove_duplicates function
numbers_test = [1, 2, 3, 2, 4, 3, 5]
test_result = remove_duplicates(numbers_test)
print(f"Test Result: {test_result}")

numbers_ duplicate = [1, 1, 2, 3, 2]
duplicate_result = remove_duplicates(numbers_duplicate)
print(f"Duplicate Result: {duplicate_result}")
```

This Python code defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a list comprehension to filter out repeated elements and returns the unique ones. The code also includes two test cases, one with regular numbers and another with duplicate values, to verify the correctness of the remove_duplicates function.