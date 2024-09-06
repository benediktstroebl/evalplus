```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list"""
    new_list = []
    for i in range(0, len(numbers)): 
        if i % 2 == 0:
            new_list.append(numbers[i])
        else: 
            new_list.append(numbers[i]) + delimeter
    return new_list
```