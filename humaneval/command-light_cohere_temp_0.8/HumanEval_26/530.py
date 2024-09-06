```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of integers.
    Args:
        numbers: list of integers
    Returns: list of unique integers without duplicates.
    """
   
    duplicate-free set,
        numbers[:] = list(set(numbers))
    return numbers[:]

# Tests
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```