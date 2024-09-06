```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The `filter_integers` function takes a list of values of any type and returns a list of integers. It utilizes Python's list comprehension to iterate over each value `x` in the input `values` list. For each value `x`, it checks if the value is an instance of the `int` class using the `isinstance()` function. If it is an integer, it includes `x` in the resulting list. The resulting list, containing only the integer values from the input, is then returned as the output. 

This approach allows the function to filter out any non-integer values from the given list, such as strings, floats, dictionaries, or lists, and return a list containing only the integer values.