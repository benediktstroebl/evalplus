```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from the input list.
    Args:
        numbers (List[int]): list of integers.
    Returns: list with all duplicates removed.
    """
    note: the order of elements remains the same
    """
    return [element for element in numbers if element not in numbers[numbers]]

# Sample test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]

numbers = [1, 2, 3, 4, 1, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]

numbers = [10, 2, 20, 10, 10]
print(remove_duplicates(numbers))  # Expected output: [10, 20]

numbers = [1, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]
```

This script defines a function called `remove_duplicates`, which takes a list of integers as input and returns a new list with all duplicate elements removed. The function uses a `set` comprehension to filter out duplicate elements. The test cases demonstrate the basic usage of the `remove_duplicates` function, passing different lists and expecting the output to have the unique elements.