```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_values = [item for item in values if isinstance(item, int)]
    return int_values
```

The function calls `isinstance()` for each item in the input list to determine if it is an instance of the `int` class, and then filters out the `int` values accordingly. The resulting filtered list is then returned. 
This approach ensures that only elements that are explicitly of type `int` are included in the output, regardless of any other data that may be in the input list. 

Here is an example of how to use this function:
```python
values = ['a', 3.14, 5, 'foo', 7.7, [1, 2], (3, 4)]
print(filter_integers(values))
```

The output will be:
```
[5, 7]
```