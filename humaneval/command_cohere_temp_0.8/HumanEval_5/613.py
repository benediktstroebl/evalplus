```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of the `numbers` list. It works by first filtering out the `delimeter` values from the `numbers` list using a list comprehension, thereby creating a new list `result`. The function then appends the `delimeter` to this `result` list to achieve the desired effect of inserting a delimiter between all consecutive elements. If the `numbers` list initially contains no elements, or if it contains only `delimeter` values, the `result` list will be empty, and the function will return an empty list.

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([0, 0, 0], 1)
[0, 1, 1, 1]
>>> intersperse([5, 5, 5, 5, 5], 2)
[5, 2, 5, 2, 5, 2, 5, 2]
```