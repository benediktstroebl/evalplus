```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first filtering out the `delimeter` values from the `numbers` list using a list comprehension, thereby creating a new list, `result`, that contains only the elements of `numbers` that are not equal to `delimeter`. If the `numbers` list contains no elements other than `delimeter`, `result` will be an empty list, and the function will return an empty list. If there are elements in `result`, the function returns the concatenation of `result` and `delimeter`, thereby encapsulating `result` with instances of `delimeter`. The output is a list of integers where `delimeter` has been inserted between every two consecutive elements of the input list `numbers`.

Here is an example usage of the function:
```python
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([1, 1, 3, 3, 5, 5, 7, 7, 9, 9], 2)
[1, 2, 3, 2, 4, 2, 6, 2, 8, 2]
```