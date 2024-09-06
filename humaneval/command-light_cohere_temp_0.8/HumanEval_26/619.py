```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes all elements that occur more than once in a list of integers.
    Retuns a list with distinct integers.
    """
    list of integers with duplicates removed.
    """
Input list of integers is modified in place.
    """return numbers[:][:new_set(numbers. iss unique()]:numbers,```

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]

numbers = [1, 2, 3, 2, 4]
test_remove_duplicates()
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a list of integers with duplicates removed. The function uses the use of the `set_unique` method to remove duplicates and returns the new list. The `test_remove_duplicates` function tests the `remove_duplicates` function by passing a list of integers and asserting that the result is correct.