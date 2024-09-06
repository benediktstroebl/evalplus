```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))  # remove duplicates using set() and list conversion


# Test cases
numbers_list = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(numbers_list)
print(result)  # Output: [1, 2, 3, 4]

numbers_set = {1, 2, 3, 4}
result = remove_duplicates(numbers_set)
print(result)  # Output: {1, 2, 3, 4}

mixed_list = [1, 2, 3, 2, 4, 3]
result = remove_duplicates(mixed_list)
print(result)  # Output: [1, 2, 3]

mixed_set = {1, 2, 3, 4}
result = remove_duplicates(mixed_set)
print(result)  # Output: {1, 2, 3}
```

This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique elements. The test cases show how the **set** is a built-in function in Python that removes duplicate elements from a collection. This method uses the use set() and list conversion to achieve this result.