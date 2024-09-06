```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [item for item in values if isinstance(item, int)]
    return integers
```

The function calls `isinstance()` for each item in the input list and filters out items that are not of type `int`. The resulting list of integers is then returned. 

To follow the specified code style, here is an example of how you can use the function:
```python
values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))
```

This would output the following:
```
[1, 2, 3]
```