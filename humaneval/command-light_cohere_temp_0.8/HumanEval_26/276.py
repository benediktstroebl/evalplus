```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return list(numbers)


def test_remove_duplicates(numbers: List[int]) -> None:
    expected = [1, 3, 4]
    got = remove_duplicates(numbers)
    assert got == expected, f"Expected {expected}, but got {got}"


# Example usage:
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates(numbers)
```
This code defines a function `remove_duplicates` that removes duplicate elements from a given list of integers. The function sets all elements in the input list to a unique set, and then converts it back to a list. The `test_remove_duplicates` function provides tests for the `remove_duplicates` function, ensuring its correctness. 
The test function compares the expected list with the result of calling `remove_duplicates` and raises an assertion error if the two lists are not equal.