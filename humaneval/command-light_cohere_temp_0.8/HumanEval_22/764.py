```python
from typing import List
def filter_integers(values):
    return [int(x) for x in values if x.isinstance(int)]
```

This function takes a list of any Python objects, and returns a new list containing only the integers from the input. It utilizes the same isinstance() to check if each element is an instance of int, and converts it to an int before returning it. This ensures that only valid integer values are included in the output.