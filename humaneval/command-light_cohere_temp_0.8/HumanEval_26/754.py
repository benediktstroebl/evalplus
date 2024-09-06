```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers.
    input: numbers = [1, 2, 3, 2, 4, 3]
    output: [1, 3, 4]
    """
    return list(set(numbers))
```