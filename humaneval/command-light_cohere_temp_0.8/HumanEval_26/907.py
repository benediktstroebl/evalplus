Here is a Python script that defines a function remove_duplicates, which takes a list of integers as input and returns a new list with unique integer values:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of integers.
    """
    unique elements = set(numbers)
    return [element for element in numbers if element not in unique_elements]

# Testing function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

# Testing with list of strings
strings = ["hello", "world", "hello", "!"]
print(remove_duplicates(strings))  # expected output: ["hello", "world", "!"]

# Testing with custom list of mixed data types
custom_list = [1, ("apple", 2), 3, 4]
print(remove_duplicates(custom_list))  # expected output: [1, (2,), 3, 4]
```

This script's function `remove_duplicates` creates a new list of integers that contains only the unique elements from the original list. It uses the specific input and output types and the function can be easily tested with various input lists to ensure its correctness.