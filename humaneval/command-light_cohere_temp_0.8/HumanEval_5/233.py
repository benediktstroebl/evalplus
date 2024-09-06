```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result
```
This Python function, `intersperse`, takes a list of integers and a delimiter as input and returns a new list with the integers separated by that delimiter. The function works by iterating through the input list, checking if the current element is the middle element of a pair, and if it is, appending the element and the delimiter to the result. If the element is not the middle, it is appended as the next element.