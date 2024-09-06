```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The `filter_integers` function takes a list of values of any type and returns a list of integers. It utilizes Python's list comprehension to iterate over each value `x` in the input `values`, and checks if the value `x` is an instance of the int class, using the `isinstance()` function. If it is an integer, it includes `x` in the `result` list, otherwise it skips it. The final `return result` line returns the list of integers. 

This function is self-contained and can easily be copied and pasted into a Python environment to filter a list of values only consisting of integers.