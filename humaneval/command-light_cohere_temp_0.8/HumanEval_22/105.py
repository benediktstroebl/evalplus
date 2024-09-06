```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function
values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
print(result)  # Output: [1, 2, 3, 5]
```