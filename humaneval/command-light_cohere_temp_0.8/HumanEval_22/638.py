```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function with a variety of input values
values_test = [
    ['a', 3.14, 5], [1, 2, 'abc'], [1, 2, 3, '123'], [(), []]
)

print(filter_integers(values_test))  # Expected output: [5, 1, 2, 3, '123']
```