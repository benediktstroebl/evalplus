Here's a self-contained Python function that filters integers from a list of various types:
```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]
```

This function accepts a list of values and returns a new list containing only the integers from the input. It utilizes the fact to check if a value is an instance of int. The function then returns a list containing only the integers from the input list.