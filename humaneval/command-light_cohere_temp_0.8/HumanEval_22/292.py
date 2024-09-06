```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [1, 2, 3]]
result = filter_integers(values)
print(result)  # Expected output: [1, 2, 3]
```