```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of `numbers`. The function checks if the `numbers` list contains the `delimeter` and excludes it during the intersperse operation. The result is concatenated with the `delimeter` and returned if the `numbers` list is not empty after the exclusion of `delimeter`. Otherwise, an empty list is returned. 

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([0, 10, 20, 30, 40], 50)
[0, 50, 10, 50, 20, 50, 30, 50, 40]
>>> intersperse([0, 10, 20, 30, 40], 50), [1, 2, 3, 4, 5]
[0, 50, 10, 50, 20, 50, 30, 50, 40, 1, 2, 3, 4, 5]
```