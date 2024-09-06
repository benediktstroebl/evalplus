```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It utilizes Python's list comprehension feature to filter out items that are not instances of the int type. The `isinstance()` function is used to check if each item in the list is an instance of the `int` class, and if so, it is included in the new list. Finally, the function returns the resulting list of integers. 

Here is an example usage of the function:
```python
values = ['a', 3.14, 5, 'yes', 1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # Output: [5, 1, 2, 3]
```

This will print the list `[5, 1, 2, 3]`, which is expected, since the given list contains integers 5, 1, 2, and 3, and all other elements (strings, float, and objects) are filtered out.