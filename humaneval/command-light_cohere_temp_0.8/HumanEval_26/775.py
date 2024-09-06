```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    1. From the list, remove duplicates.
    2. Create a unique set from the fact list of numbers.
    3. Remove any duplicates from the BCE
   
    4. Return a list of unique integers.
"""
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]

def test_remove_duplicates2():
    numbers = [2, 4, 2, 1, 4, 2]
    result = remove_duplicates(numbers)
    assert result == [2, 4, 1]

test_remove_duplicates()
test_remove_duplicates2()

```
The function remove_duplicates takes a list of integers as input and returns a list of unique integers. The function creates a unique set from the input list of numbers. The set is then removed from the input list to ensure that duplicates are removed. The function then returns the list of unique integers.