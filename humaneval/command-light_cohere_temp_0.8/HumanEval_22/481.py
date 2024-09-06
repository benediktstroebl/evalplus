Here's a self-contained Python function that filters integers from a list of any values:
```python
from typing import List

def filter_integers(values:
    returns = List[int]
    return [x for x in values if isinstance(x, int)]
```
This function takes a list of any type as its argument and returns a new list containing only the integers present in the input. The type is also guaranteed to be of type int.