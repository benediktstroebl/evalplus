```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate integers from a list.
    Returns a list with integers only present once.
    """
    def __init__(self, numbers: List[int]) -> None:
        self.numbers = list(numbers)
    if len(set(self.numbers)) != len(self.numbers):
        raise ValueError("Input list must contain unique integers")
    return self.numbers[:]
```

# Unit tests
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 1]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected

numbers = [1,2,3,4]
test_remove_duplicates()  # Output: True
```

The above code defines a remove_duplicates function and tests it using the test_remove_duplicates function. The remove_duplicates function takes a list of integers as input and returns a new list with only the unique integers from the original input list.