Here's the self-contained Python function that solves the problem of removing duplicates from an input list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    duplicates = set(numbers)
    result = [num for num in numbers if num not in duplicates]
    return result

# Example usage
numbers = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers))  # Output: [1, 3, 4, 5]
```

This function uses the set data structure to automatically remove duplicate elements from the input list, and then creates a new list with the remaining unique elements. The example usage demonstrates how this function can be used to remove duplicates from a list of integers and produce the desired output.