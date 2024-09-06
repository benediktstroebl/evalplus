```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimeter)
        else:
            result.append(num)
    return result
```
This function takes a list of integers and a delimiter as input, and returns a list of integers with the delimiter inserted between every other two consecutive elements. The function works by iterating through the input list, checking if the current element is the first element (i. If so, it appends the delimiter to the result list. If it's not, it appends the current element to the result list.