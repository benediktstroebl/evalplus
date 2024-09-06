Here is a self-contained Python script that solves the problem of removing duplicates from a list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    duplicates = set(numbers)
    return [num for num in numbers if num not in duplicates]

# Example function test
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert expected == result
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses the example, it creates a new set of integers and then uses the `set` function to create a new list of elements that are not in the set. The function then returns a list of integers that are not in the set.