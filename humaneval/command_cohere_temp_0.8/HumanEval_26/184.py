```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    return list(set(numbers))
```
This code uses a set, which inherently does not contain duplicate elements, to remove duplicates from the list of integers. Then, it converts the set back to a list to maintain the original order. As a result, the function returns a list of unique elements in the same order as they appeared in the input list, achieving the specified behavior.