```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers."""
    return [i for i in values if isinstance(i, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [0], [1, 2, 3]]
print(filter_integers(values))  # Output: [1, 2, 3]
```