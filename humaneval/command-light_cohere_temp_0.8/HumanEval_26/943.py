```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements as in the input.
    """
    return the remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return [n for n in numbers if n not in set(numbers)]
```