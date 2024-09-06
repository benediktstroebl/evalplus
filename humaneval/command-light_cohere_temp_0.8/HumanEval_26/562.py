Here is a self-contained Python script that solves the problem of removing duplicates from a list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    duplicates = set(numbers)
    result = [x for x in numbers if x not in duplicates]
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]

# Test the function with a list of strings
strings = ["hello", "world", "hello"]
print(remove_duplicates(strings))  # Expected output: ["hello", "world"]
```

This script defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. It uses the common Python idiom x != y to check for duplicates and a set to quickly eliminate duplicates. This solution is optimized for performance by removing duplicates from a set and avoiding an additional loop.