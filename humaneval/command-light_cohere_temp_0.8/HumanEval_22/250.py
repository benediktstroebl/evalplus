```python
from typing import List

def filter_integers(values):
    return [int(x) for x in values if x.isinstance(int)]

# Test the function
values = [1, 2, 'three', 3.14, 5]
result = filter_integers(values)
assert len(result) == 5, "Error: Function does not filter integers correctly."
```