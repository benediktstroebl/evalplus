```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements as the value.
    """ Here's a a list of integers"""
    return [num for num in set(numbers) if num not in numbers[numbers]])
```