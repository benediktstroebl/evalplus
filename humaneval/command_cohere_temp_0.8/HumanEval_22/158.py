```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
```

The function employs a list comprehension in conjunction with the `isinstance()` function to filter out integers from the input list. The resulting list of integers is then returned. This implementation provides a straightforward way of extracting integers from a diverse list of values, whilst maintaining type safety through the use of typing annotations.