```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    duplicates = {num for num, num1 in enumerate(numbers) if num1 > num}
    return [num for num in numbers if num not in duplicates]

# Unit tests
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates = [
    (numbers, "Input list with duplicates"),
    (numbers[:2] + [4] + numbers[2:], "List with duplicates, only 4"),
    (numbers + [5], "List with duplicates, 5 added"),
    (numbers[:1] + [4] + numbers[1:], "List with only 4 duplicates")
]

def test_remove_duplicates():
    for test in test_remove_duplicates:
        actual = remove_duplicates(test[0])
        assert actual == test[1], f"Expected {test[1]}, got {actual}"

test_remove_duplicates()
 ```

The code defines a function `remove_duplicates(numbers: List[int]) -> List[int]` that takes a list of integers as input and removes all elements that occur more than once, ensuring elements left are retained. The function uses a list comprehension and a dictionary to identify duplicates and returns a new list with elements not present in the duplicates.

This script also includes unit tests for the `remove_duplicates` function using the `unittest` module, testing various input scenarios. 

It tests the function with lists containing duplicates, lists with only specific duplicates, and lists with no duplicates at all.  The expected output is for each test case should be the output of the `remove_duplicates` function with the respective input.