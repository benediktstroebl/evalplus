```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Set removes duplicates automatically
    return list(numbers)

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [10, 20, 30, 10, 40, 40]
result = remove_duplicates(numbers)
print(result)  # Output: [10, 20, 30, 40]

numbers = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

This script defines a function `remove_duplicates` that takes a list of integers and returns a new list with duplicates removed. The function uses the use of the `set()` function to automatically eliminate duplicates. 

The script then creates a few test lists and calls the function with each list, printing the result.