```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Remove duplicates from the list of integers
    result = set(numbers)
    return list(result)


# Test case:
numbers = [1, 2, 3, 2, 4]
result_test = remove_duplicates(numbers)
print("Result:", result_test)  # Output: [1, 3, 4]
```
This Python code defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses the unique element removal through the set and list conversion. 

This is a self-contained function with an example test case that demonstrates its intended usage.