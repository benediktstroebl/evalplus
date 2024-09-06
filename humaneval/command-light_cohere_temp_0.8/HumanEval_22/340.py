```python
from typing import List

def filter_integers(values:
    return [num for num in values if type(num) == int]

# Test the function
values = [1, 2, 3, 'abc', {}, [0, 3])
print(filter_integers(values))  # Expected output: [1, 2, 3]

# Test list comprehension with wrong types
values = [1, 2, 3, 'aaa', ['foo', 'bar'])
print(filter_integers(values))  # Expected output: []
```