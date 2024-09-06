```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It does so by using a list comprehension that checks if each element `x` in the input list `values` is an instance of the `int` class, and if so, includes it in the `result` list. Ultimately, it returns the `result` list containing only the integer values from the input.