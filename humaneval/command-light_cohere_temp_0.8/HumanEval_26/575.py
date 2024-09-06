```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers.
    set_int = set()
    # Loop through the list and add all integers to the set
    for num in numbers:
        set_int.add(num)
    # Convert the set back to the list and return it
    return list(set_int)

# Example usage
numbers = [1, 2, 3, 2, 4, 3]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and removes all duplicate elements. It achieves this by first converting all integers into a unique set using the `set()` function. Then, it converts the back to the list and returns it.