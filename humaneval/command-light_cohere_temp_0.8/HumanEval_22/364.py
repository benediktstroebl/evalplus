```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [element for element in values if isinstance(element, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [0]]
result = filter_integers(values)
print(result)  # Output: [1, 2, 3]

# Test again to validate the function signature
values = [1, 2, 3, 'abc', {}, [0], [1, 2, 'a', 3])
result2 = filter_integers(values)
print(result2)  # Output: ['1', '2', 'a', '3']
```