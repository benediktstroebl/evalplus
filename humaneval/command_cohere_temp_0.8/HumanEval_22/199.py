```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It utilizes Python's list comprehension to iterate over each value in the input list. For each value, it checks if the value is an instance of the integer class using the `isinstance()` function. If it is, the value is included in the resulting list. The comment section provides an example usage of the function, showcasing its behavior when applied to various input lists.  The function is designed to be self-explanatory, easily understood by readers, and does not require any external dependencies or additional logic. 

This approach ensures that the function can be easily understood and used by other users without relying on external code or dependencies.