Here's a self-contained Python function that filters integers from a list of various types:
```python
from typing import List

def filter_integers(values:
    ints = [i for i in values if type(i) == int]
    return ints
```

This function uses a list comprehension to filter out any values that are not of the integer type from the provided list. It tests whether an element is an integer by using the `isinstance` of `int` to check if the value is an integer.