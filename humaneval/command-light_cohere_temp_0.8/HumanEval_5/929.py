```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list. """
   
   
    function takes in a list of numbers and an integer as parameters, and it uses the intersperse built-in function to add a delimiter between every two numbers in the list. It then returns the process a new list with the original numbers, with the added delimiter.

Example usage:
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```