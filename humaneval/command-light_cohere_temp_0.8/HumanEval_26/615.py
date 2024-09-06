```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    duplicate_free = [n for n in numbers if n not in set(numbers)]
    return [n for n in numbers if n not in duplicate_free]

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
```  The provided code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The function utilizes the duplicate detection by creating a set of the input numbers and checking if each number is present in the set. The `test_remove_duplicates` function verifies the functionality of the `remove_duplicates` function by asserting that it correctly removes duplicate values from the given list of integers.