```python
from typing import List

def filter_integers(values:
        return [x for x in values if isinstance(x, int)]

# Test the function with various data types
values_test = [['a', 3.14, 5, (1, 2, 3, 'abc', [ }, []])
print(filter_integers(values_test))  # Output: [5, 1, 2, 3]

# Another test with complex objects
class Complex:
    a: int
    b: str
    def __init__(self, a, b):
        pass

obj_values_test = [Complex(1, 'abc'), Complex(2, 'b')]}
print(filter_integers(obj_values_test))  # Output: []
```