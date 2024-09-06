```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only the entry one more than the number 1 in the input list.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers = [num for num in numbers if num != 1]
    return numbers

# run test function
def test(numbers: List[int]):
    expected = [1, 3, 4]
    got = remove_duplicates(numbers)
    assert expected == got
```