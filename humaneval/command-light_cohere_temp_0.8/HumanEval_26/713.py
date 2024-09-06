```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the list.
    Input: numbers List[int],
    Output: List[int] with all duplicates removed.
    """
   
    elements that occur more than once in the list.
    """
    List comprehension: 
    numbers_without_duplicates = [num for num in numbers if num not in set(numbers)]
    return numbers_without_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
```
The `remove_duplicates` function takes a list of integers, and removes all duplicate elements. The `test_remove_duplicates` function tests the `remove_duplicates` function with a sample input list, and asserts that the function returns the correct output.