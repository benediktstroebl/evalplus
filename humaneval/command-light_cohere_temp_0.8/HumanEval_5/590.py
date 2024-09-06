```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list """
    return [i+delimiter for i, adjacent in enumerate(numbers, 1)] + [numbers[-1]]
# Test the function with various inputs
numbers = [1, 2, 3, 4, 10, 2]
delimiter = 10
result = intersperse(numbers, delimiter)
print(result)
```