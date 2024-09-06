```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are the first four numbers: (0,1,2,3)
    >>> sort_numbers('three one five')
    'one three five'
    """
    return numbers.map(num => sorted(nums) for nums in [int(n) for n in numbers.list() if nums in [0,1,2,3])
```