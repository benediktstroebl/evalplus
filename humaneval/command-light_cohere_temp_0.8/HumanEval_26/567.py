```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only theufficates once
    """
    return [num for num in numbers if num not in numbers[numbers.set()]]
```