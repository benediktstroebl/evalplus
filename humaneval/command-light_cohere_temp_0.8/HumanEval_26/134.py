```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only elements left as in the input.
    return [unique(numbers)
    """

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 1, 4]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected

#run the test
test_remove_duplicates()

```

This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers. The function utilizes the unique function from the set module to remove any duplicates and returns the unique elements. The code also includes a function `test_remove_duplicates` which tests the `remove_duplicates` function by passing a list of integers and asserting that the result is indeed unique.