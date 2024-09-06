```python
from typing import List

def filter_integers(values):
    return [int(x) for x in values if x.isinstance(int)]
```

This function takes a list of values, and returns a new list containing only the integers from the input. It uses theis filtered list comprehension and the `isinstance()` function to only return integers from the input list.