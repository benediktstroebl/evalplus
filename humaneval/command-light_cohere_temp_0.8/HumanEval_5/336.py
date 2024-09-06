```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Example list must only elements of integers
    """
    result = [x for x in numbers[::2] + [x] + [numbers[1::2]] + [x] if type(numbers) is list else
        numbers]
    return result
```