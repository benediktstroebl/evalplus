```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Parameters: numbers (list of integers) and delimiter (int).
    Returns: A list with integers separated by the delimiter.
    """
Example:
    >>> intersperse([1,2,3],2)
    [1,2,2,3]
    """
    return [i+delimiter for i,delimiter in zip(numbers,delimeter)]

# unit tests
numbers = [1, 2, 3]
delimiter = 2
result = intersperse(numbers, delimiter)
print(result)  # expected output: [1, 2, 2, 3]
``` 
This Python code implements a function `intersperse` that adds a separator between consecutive elements in a list. The purpose of this code is to produce a new list with the elements of the original list separated by the specified separator. 

A test case is provided to show how the function works with a sample list of integers.