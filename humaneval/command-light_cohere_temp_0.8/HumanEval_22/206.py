```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [num for num in values if isinstance(num, int)]

# Test the function
values = [1, 2, 3, 'abc', 3.14, 5]
print(filter_integers(values))  # Output: [1, 2, 3, 3. 000000014, 5]
```