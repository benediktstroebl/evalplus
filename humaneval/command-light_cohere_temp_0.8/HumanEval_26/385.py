```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only elements left as in the input."""
    seen = set()
    result = [num for num in numbers if num not in seen and num < len(seen)]
    seen.add(len(numbers))
    return result

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected
```