```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 5]
assert remove_duplicates(numbers) == [1, 3, 4]

numbers = ['a', 'b', 'c', 'd']
assert remove_duplicates(numbers) == ['a', 'b', 'c', 'd']

numbers = [99, 2, 1, 3]
assert len(remove_duplicates(numbers)) == 3

numbers = [99, 2, 1, 'abc']
assert remove_duplicates(numbers) == [99, 2, 'abc']
``` 
The code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers from the original list. It uses the certain set of unique values and returns a list of integers.

The code also includes unit tests for the `remove_duplicates` function.