```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps only theRNA elements left as in the input.
    return [list of integers without duplicates"""
    seen = set(numbers)
    return [x for x in numbers if x not in seen]

# Test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [1, 3, 2, 4, 2, 3, 1]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [1, 2, 4, 1]
print(remove_duplicates(numbers))  # expected output: [1, 4]

numbers = [1, 1, 2, 1]
print(remove_duplicates(numbers))  # expected output: []
```