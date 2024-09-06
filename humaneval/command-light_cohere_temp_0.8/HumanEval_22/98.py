```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [0])
assert filter_integers(values) == [1, 2, 3]
values = [3.14, 5, 'a']
assert filter_integers(values) == [5]
```