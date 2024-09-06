```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes elements that occur more than once from a list of integers.
    Input: numbers = [1, 2, 3, 2, 4]
    Output: [1, 3, 4]
    """
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.isdefault]]
 same:
        seen.add numbers
```
```