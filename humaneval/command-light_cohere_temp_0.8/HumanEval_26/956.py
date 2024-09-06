```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate elements from a list of integers.
    >>> removes( [1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return [n for n in numbers if n not in numbers[numbers.count(set())]


def test_remove_duplicates():
    """ Test the remove_duplicates function """
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    actual = remove_duplicates(numbers)
    assert expected == actual
```