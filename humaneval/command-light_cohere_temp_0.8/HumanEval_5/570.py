Here is a self-contained Python script that solves the problem of inserting a number `delimiter` between every two consecutive elements of the input list:

```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for num in numbers:
        if len(result) < 2:
            result.append(num)
        else:
            result.append(delimiter)
            result.append(num)
    return result
```

This script defines a function called `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input, and returns a new list with the elements of the input list interspersed with the `delimiter` at every other pair of consecutive elements. 

The function uses a loop to iterate through the input list, and appends the current element to the result list only if the length of the result list is less than 2.  If the length of the result list reaches two elements, the `delimiter` is appended, and the next element is appended to the result list.