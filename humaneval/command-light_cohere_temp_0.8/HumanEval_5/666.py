```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list."""
    result = [num1, num2, delimiter, num3]  # Use list comprehension to create consecutive tuple
    while num2 != None:
        result.append(num2)
        num1 = num2
        num2 = delimiter
    result.append(num3)
    return result
```
This function takes two arguments: a list of integers `numbers` and an integer `delimiter` that will be used as a separator between every two consecutive elements. The function returns a a modified list with the given `delimiter` inserted between every two elements.