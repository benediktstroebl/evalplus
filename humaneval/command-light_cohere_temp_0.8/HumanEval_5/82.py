```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list.
    Returns a other list of the
    """
    numbers = [1, 2, 3, 4, 5]
    return [i, delimiter, j] for i, j in enumerate(numbers, 2)
```  This function does the following:
- Takes a list of integers and a delimiter integer as input. 
- Uses the enumerate function to create a new list where the ith index of every pair of consecutive elements is replaced with the delimiter. 
- The final list is returned.