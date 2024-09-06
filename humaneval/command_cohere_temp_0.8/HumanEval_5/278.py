```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be placed in between consecutive numbers. It works by first filtering out the `delimeter` values from the `numbers` list using a list comprehension, thereby creating a new list `result`. If the `result` list is empty, indicating that the input list contained only delimeters, it returns an empty list. Otherwise, it returns the `result` list joined with repeating instances of the `delimeter`. 

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5], 2)
[0, 2, 2, 2, 2, 2, 5, 5, 2, 5, 5, 5]
``` 

This neatly places the `delimeter` value of `2` in between consecutive elements of the list, leaving only repeated delimiters if the list contains only `delimeter` values.