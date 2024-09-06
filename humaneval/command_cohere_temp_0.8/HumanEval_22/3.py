```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It uses a list comprehension to iterate over each element in the input list and checks if the element has an integer type using the `isinstance()` function. If the element is of type `int`, it is included in the resulting list.

Here is an example usage of the function:
```python
values = ['a', 3.14, 5, 'foo', 7, 2.5]
result = filter_integers(values)
print(result)
```

The output will be:
```
[5, 7]
```