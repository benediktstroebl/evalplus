```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ 
    Remove all duplicate elements from the list.
    Input: list of integers.
    Output: list of distinct integers without duplicates
    """
    numbers = set(numbers)
    return [x for x in numbers if x not in numbers]

# Test the remove_duplicates function
test_remove_duplicates = []
test_remove_duplicates.append([1, 2, 3, 2])
test_remove_duplicates.append([4, 1, 3, 4])
print(remove_duplicates(test_remove_duplicates)) 
```