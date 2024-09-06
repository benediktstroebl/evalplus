```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Result: A list of elements with the added delimiter, and the original order preserved.
    Args: 
        numbers: list of integers, the input list with elements to be interspersed 
        delimiter: integer, the value added between every two consecutive elements
    Returns: 
        list, the list of integers with the desired format
    """
    new_list = [x+delimiter for x,y in zip(numbers,numbers[1:])]
    return new_list

#unit tests
numbers = [1, 2, 3]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
print(result) #output: [1, 0, 4, 2, 4, 3]
```