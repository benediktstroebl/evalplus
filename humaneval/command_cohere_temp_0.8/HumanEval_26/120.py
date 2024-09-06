```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not seen.add(num):
            result.append(num)
    return result
```

The `remove_duplicates` function uses a set, `seen`, to keep track of seen integers. It iterates through the input list, checking if each integer is in the set. If the integer is not in the set, it is added to the set and also added to the result list. If the integer is already in the set, it is skipped.

The tests for this function would typically be a few calls to the function with various input lists, verifying that the output lists are correct. 
Here's an example:
```python
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([0, 0, 1, 2, 1, 3, 4, 3, 5]) == [0, 1, 2, 3, 4, 5]
    assert remove_duplicates([10, 5, 1, 15, 1, 2, 3, 4, 4, 5, 5, 3]) == [10, 5, 1, 2, 3, 4, 5]
``` 

This test suite would ensure that the `remove_duplicates` function works correctly for a variety of input lists, and the expected output lists are provided as assertions.