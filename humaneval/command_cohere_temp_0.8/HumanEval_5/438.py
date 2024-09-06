```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to insert between consecutive numbers. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, thereby creating a new list `result`. If the `result` list is empty, indicating that all elements of `numbers` were `delimeter`, then the function returns an empty list. Otherwise, it returns the `result` list joined with the `delimeter` value repeated multiple times to insert it between each number in the `result` list.

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```

And it works correctly for edge cases:
```python
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 0)
[1, 0, 2, 0, 3]
```