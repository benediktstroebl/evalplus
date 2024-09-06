Here's a self-contained Python script with a function that solves the problem of inserting a specified delimiter between every two consecutive elements in a list:
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for n in numbers:
        if len(result) > 1:
            result.append(delimeter)
        result.append(n)
   return result
```
Do you need help with anything else?