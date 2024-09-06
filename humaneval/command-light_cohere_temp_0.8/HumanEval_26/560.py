```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and not in numbers[0]]
    seen.add(numbers[0])
    return result


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert len(result) == 3
    assert set(result) == {1, 3, 4}


if __name__ == "__main__":
    test_remove_duplicates()
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all integers that are not already in the original list and are not equal to the first element in the list. The function uses a Python's `set` data structure to keep track of duplicate elements and uses the set to determine if an element is a duplicate or not. The `test_remove_duplicates` function tests the `remove_duplicates` function by passing in a list of integers and asserting that the resulting list contains only unique integers.