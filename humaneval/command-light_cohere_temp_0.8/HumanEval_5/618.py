Here is a Python script that solves the markdown code block problem:
```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    >>> intr      = []
    >>> intr      = [1,2,3]
    >>> intersperse( intr, 2)
    [1, 2,  2, 3]
    """
    new_list = [num + delimeter for num in numbers] + [num + delimeter for num in numbers[1:]]
    return new_list[:]
``` 
This code defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a list with the numbers separated by the given delimiter. The code creates a list comprehension to add the delimiter between the first and second elements, and then the second and third elements, creating the desired output.