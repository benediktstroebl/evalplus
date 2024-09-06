```python
from typing import List

def filter_integers(values: List[Any]):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [['a', 3.14, 5, 1, 2, 'abc', {}, []]
print(filter_integers(values))  # Output: [5] [1, 2, 3]
```