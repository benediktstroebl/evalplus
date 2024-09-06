```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [i for i in values if isinstance(i, int)]

# Example usage:
values = [1, 2, 3, 'abc', {}, [0, 'five', 3.14]]
print(filter_integers(values))  # Output: [1, 2, 3, 0, 5]
```