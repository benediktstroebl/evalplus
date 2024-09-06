```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from the list of integers and return a new list.
    :duplicates are in the list are removed. 
    """
    new list will a set of distinct integers.

# Testing the function
numbers = [1,2,3,2,4,3,2]
assert remove_duplicates(numbers) == [1, 2, 3, 4]

numbers = [1,2,3,3,4,5]
assert remove_duplicates(numbers) == [1, 2, 3, 4, 5]

numbers = [1,2,3,4,2,1]
assert remove_duplicates(numbers) == [1,2,3,4]

# Test with a list of strings
numbers = ["a", "b","c", "d"]
assert remove_duplicates(numbers) == ["a", "b", "c", "d"]
```