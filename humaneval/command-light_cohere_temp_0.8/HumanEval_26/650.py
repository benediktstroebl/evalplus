```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements as the all elements left as in the input list.
    """
    test that the list contains only integers, and all numbers should appear at most once.
    """
    test with List([4, 2, 2, 3, 1]) as the input list
    assert remove_duplicates([4, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates([4, 2, 1, 3]) == [1, 2, 3]
    assert remove_duplicates([4, 2, 3, 2]) == [1, 2, 3]
    assert remove_duplicates([4, 4, 4]) == [4]
    assert remove_duplicates([4, 4, 4, 2]) == [4]
    assert remove_duplicates([4, 2, 1, 3, 4]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]
    return numbers
```