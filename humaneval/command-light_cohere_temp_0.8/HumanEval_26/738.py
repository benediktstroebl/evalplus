```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 0]

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 5]
test_remove_duplicates = [
    "It should return a list containing all positive integers",
    "after removing duplicates",
    "Result: [1, 3, 4]"
]

def test_remove_duplicates_func(*args):
    actual_numbers = remove_duplicates(args)
    assert actual_numbers == test_remove_duplicates

test_remove_duplicates_func(*numbers)
```
This Python script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with all positive integers after removing duplicates. The function is then accompanied by a series of unit tests that aim to validate the correctness of the `remove_duplicates` function.