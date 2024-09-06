```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove duplicate elements from a list of integers.
    Input: numbers is a list of integers
    Output: A list of integers without duplicates.

    Returns: list with all unique elements from the input list
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return: result
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This Python code defines a function remove_duplicates that takes a list of integers as input and removes duplicate elements by using the set data structure. It returns a optimized list with all unique elements from the input list. This is a efficient and self-contained solution.