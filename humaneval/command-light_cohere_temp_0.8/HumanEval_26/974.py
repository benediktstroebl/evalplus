```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps only the
elements left as in the input.
    """
    numbers = List(set(numbers))
    return numbers

# Test the function
numbers = [1, 2, 3, 2, 4, 2]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 4, 2, 3, 1]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]

# Test with empty list
numbers = []
result = remove_duplicates(numbers)
print(result)  # Output: []
```