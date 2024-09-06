```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from a list of integers.
    unique: numbers = [1, 2, 3, 2, 4, 2, 1, 5, 6]
    return remove_duplicates(numbers)
    [2,3,4]
    """
    return [n for n in numbers if n not in numbers[numbers.count(set())]

# Tests
numbers = [1, 2, 3, 2, 4, 2, 1, 5, 6]
print(remove_duplicates(numbers))  # [2,3,4]

numbers = [1,2,3,4,3,2]
print(remove_duplicates(numbers))  # [1,2,3,4]

numbers = [1,1,2,3]
print(remove_duplicates(numbers))  # [1,2,3]
```