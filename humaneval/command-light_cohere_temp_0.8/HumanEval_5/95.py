```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Time to test my good list comprehension style function
    >>> Numbers = [1, 2, 3,4,5]
    Numbers = [x + i for i, x in zip(Numbers, Numbers[1:])]
    Numbers = [x for x in Numbers if x != len(Numbers) // 2]
    return Numbers
```