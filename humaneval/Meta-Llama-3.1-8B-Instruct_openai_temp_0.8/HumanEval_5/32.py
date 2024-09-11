```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(delimeter)
        result.append(numbers[i])
    
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This Python script defines a function `intersperse` that inserts a specified number (`delimeter`) between every two consecutive elements of the input list `numbers`. The function works by initializing the result list with the first element of the input list, then iterating over the rest of the input list, appending the delimeter and the current element to the result list. If the input list is empty, the function returns an empty list.