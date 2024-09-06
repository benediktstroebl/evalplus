```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The function `filter_integers` takes a list of values of any type as input and returns a list of integers. It utilizes Python's list comprehension capability to filter out non-integer elements. This function efficiently removes non-integer items from the given list irrespective of their data type, such as strings, floats, dictionaries, or even other lists. 

This solution encompasses the functionality to solve the problem in a single function and provides an illustrative docstring to explain its purpose.