```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    """
    unique_numbers
    list and return a new list without duplicates"""
    return list(set(numbers))

# Example test cases:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]

numbers = [4, 3, 2, 1, 5]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 4, 5]

numbers = [1, 2, 3, 4, 2]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
```
This Python script defines a function called `remove_duplicates` that takes a list of integers as input and removes all duplicate elements, using the `set()` function to create a unique set of the elements. The function then returns a list of the elements without duplicates. The test cases demonstrate the expected output of the function.