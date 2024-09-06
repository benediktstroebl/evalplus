```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 0 and num not in numbers]

# Test the function
test_remove_duplicates = [1, 2, 3, 2, 4, 2, 3]
result = remove_duplicates(test_remove_duplicates)
assert result == [1, 3, 4]
```

This function, `remove_duplicates`, takes a list of integers as input and returns a new list with duplicate numbers removed. It uses the For method `set()` to create a set of unique numbers, and then uses list comprehension to filter out the elements that are not in the set and are greater than 0.

Note that the function is self-contained, and it does not require any external variables or other functions to be defined.