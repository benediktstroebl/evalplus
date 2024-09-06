```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [int(x) for x in values if x.isinstance(int)]
```

This Python script defines a function named `filter_integers` that filters a list of values, ensuring only integers are returned.  The function employs the basic list comprehension and the `isinstance()` method to filter out non-integer values from the input list.