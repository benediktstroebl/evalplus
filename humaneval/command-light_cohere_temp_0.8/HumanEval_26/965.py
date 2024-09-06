```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list.
    Args:
        numbers (List[int]): list of integers.
    Returns: modified list with unique elements.
    """ Returns the unique elements
    elements that do not occur more than once.
    """
    modified list with unique elements, removes duplicates.
    return list(set())
    ```

# Example test
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

test_numbers = [1, 1, 2, 3, 4, 3, 2]
result = remove_duplicates(test_numbers)
print(result)  # Output: [1, 2, 3, 4]

test_strings = ["a", "a", "b", "a"]
result = remove_duplicates(test_strings)
print(result)  # Output: ["a", "b"]
```

This script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with unique elements. It utilizes the basic set to find duplicates and remove them from the list.