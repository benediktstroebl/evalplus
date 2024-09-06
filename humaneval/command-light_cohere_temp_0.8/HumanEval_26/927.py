Here is a Python script with a self-contained function that solves the problem of removing duplicate numbers in a list:
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique numbers
    duplicates = set(numbers)
    # Filter the list to only include numbers that are not in the set
    return [num for num in numbers if num not in duplicates]
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 2, 5, 6]
    expected = [1, 2, 3, 4, 5, 6]
    result = remove_duplicates(numbers)
    assert expected == result
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate numbers removed. The function works by creating a set of unique numbers from the input list, then filtering the original list to only include numbers that are not in the set.

The script also includes a function `test_remove_duplicates` which tests the `remove_duplicates` function with a sample list of numbers and asserts that the expected output matches the actual output.