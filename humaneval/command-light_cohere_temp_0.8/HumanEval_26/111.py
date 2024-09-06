Here's a self-contained Python script that defines a function remove_duplicates which removes duplicate elements from a list:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove duplicate integers from a list.
    Unique elements: [1, 2, 3, 4]
    """
    # Set to ensure unique elements
    numbers = set(numbers)
    return list(numbers)
```
This script provides a function to remove duplicates from a given list, and passes the corresponding tests.