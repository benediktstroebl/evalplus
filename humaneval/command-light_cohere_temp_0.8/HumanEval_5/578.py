```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list"""
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimiter)
    result.append(num)
    return result
``` 
This function uses the Python list comprehension and itertools package to achieve the desired output. 
The list comprehension is used to loop through the input list of numbers, and for each pair of consecutive numbers, it adds the current number and then adds the delimiter to the output list. 
This approach creates the desired effect of inserting the delimiter between every two consecutive elements in the list.