```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes all duplicate elements from a list of integers. 
    Returns a same elements left as the list.
    """

    Set list of numbers and then use set() to remove all duplicate elements.
    Resulting list is every unique integer.
    """

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 4, 1]
    result = remove_duplicates(numbers)
    assert len(result) == 4
```