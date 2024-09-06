```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with a variety of values and data types
values_test = [
    ['a', 3.14, 5], [1, 2, 3, 'abc', {}, []], [float('5')]
values = [1, 2, 'three', 3, 'zero', '123']

print(filter_integers(values_test))
print(filter_integers(values))
```