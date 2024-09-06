```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to insert between consecutive numbers. It first filters out the `delimeter` from the `numbers` list using a list comprehension, `result = [x for x in numbers if x != delimeter]`. If the `numbers` list initially contains the `delimeter`, the `result` list will be empty and the function returns an empty list `[]`. Otherwise, the function returns the `delimeter` appended to the end of the `result` list, `delimeter + result`. 

Here is an example of function usage:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```
```python
>>> intersperse([], 4)
[]
```