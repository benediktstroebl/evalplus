```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove all elements that occur more than once from a list of integers.
    duplicates = set(numbers)
    return [num for num in numbers if num not in duplicates]
    """
    duplicates = set(numbers)
    return [num for num in numbers if num not in duplicates]
```
This function removes duplicate items from a list of integers and returns a new list with unique values. It uses the the from set to quickly filter out the duplicates.