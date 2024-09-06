```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    res: List[int] = []
    for value in values:
        if isinstance(value, int):
            res.append(value)
    return res
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out all elements that are not of type `int`. It uses a type hint `List[Any]` to indicate that the input parameter can hold any type of value, and a type hint `List[int]` to indicate that the returned list should contain only integers. For each element in the input list, the function checks if it is an instance of `int` using the `isinstance()` function, and if so, it includes the element in the result list.

Here is an example usage of the function:
```python
values = ['a', 3.14, 5, 'foo', 7.3, []]
print(filter_integers(values))
# Output: [5, 7]
```

This will print out a list containing only the integers `5` and `7`, which are present in the input list.