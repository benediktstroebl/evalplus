```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicates from the input list and return the unique elements.
    """
    duplicates are list of integers is assumed to be sorted in ascending order.
    """
    duplicates are removed and only the unique elements are kept.
    """ return the unique elements, sorted in ascending order.
 numbers = [1, 2, 3, 2, 4]
unique = remove_duplicates(numbers)
print(unique)  # [1, 3, 4]
```