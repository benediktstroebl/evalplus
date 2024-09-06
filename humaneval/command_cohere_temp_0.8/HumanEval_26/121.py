```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order as input. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not seen.add(num):
            result.append(num)
    return result
```

The following test cases pass:
```python
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 1, 2, 3, 4, 4, 2, 2]) == [1, 2, 3, 4]
    assert remove_duplicates([0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == [0, 1, 2, 3, 4]
```