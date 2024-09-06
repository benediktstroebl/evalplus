```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Parameters: numbers (list of integers) and delimiter (int).
    Returns: A list of integers with the 'delimiter' between every two
    consecutive elements.
    """
   
    takes list of integers numbers as its argument
    """
    return [x + i * delimeter for i, x in enumerate(numbers)]
```