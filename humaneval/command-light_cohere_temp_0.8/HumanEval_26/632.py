```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate numbers from a list.
    Input: List of integers.
    numbers = [1, 2, 3, 2, 4, 3, 1]
    return [x for x in numbers if numbers.find(x) == 0]
```