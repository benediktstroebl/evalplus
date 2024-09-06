```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [val for val in values if isinstance(val, int)]
```

The function uses a list comprehension, iterating over each value in the input list. It checks if each value is an instance of the integer class, and if so, it includes it in the resulting list. The resulting list contains only integers from the original list, filtering out any non-integer values.