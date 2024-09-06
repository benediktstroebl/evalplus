```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out all elements that are not of type `int`. It utilizes the `isinstance()` function to check if each list item is an instance of the `int` class and appends the relevant items to a new list, which is returned as the result. The function includes a docstring for clarity and better code organization.

Here is an example of how to use the function:
```python
values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
print(result)
```

Output:
```
[5, 1, 2, 3]
```