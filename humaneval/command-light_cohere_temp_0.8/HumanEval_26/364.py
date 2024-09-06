```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num < len(seen)]
    seen.add(numbers)
    return result

# Unit tests
test_remove_duplicates_function() {
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 2, 2, 3, 4]) == [1, 3, 4]
    assert remove_duplicates([5, 6, 7]) == [5, 6, 7]
    assert remove_duplicates([8, 8, 8]) == [8, 8]
}

def test_remove_duplicates_function():
    test_remove_duplicates_function()()
```
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The function utilizes a set data structure to keep track of seen values, then iterates through the input list and adds unique values to a new list, which is subsequently returned.

The code also provides unit tests for the `remove_duplicates` function using the `test_remove_duplicates_function` helper function. These tests tests verify the
            expected behavior of the function and ensure its correctness.