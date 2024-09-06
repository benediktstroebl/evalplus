```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list"""
    new_list = []
    for i in range(len(numbers)):
        if i % 2 == 0:  # Odd index
            new_list.append(numbers[i])
        else:  # Even index
            new_list.append(numbers[i])
            new_list.append(delimiter)
   return new_list
    ```