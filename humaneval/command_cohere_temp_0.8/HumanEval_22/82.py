```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The function uses a list comprehension, traverses each element in the `values` list, and checks if the element is an instance of the `int` type. If it is, it includes the element in the resulting list. The resulting list will only contain integers and won't include any other data type.