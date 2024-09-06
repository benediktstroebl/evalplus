```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values_list = [1, 2, 3, 'abc', {}, [5], [3.14] ]
 print(filter_integers(values_list))
```