```python
from typing import List
def filter_integers(values:
    return [i for i in values if type(i) == int]

# Test the function with various input values
test_values = [['a', 3.14, 5], [1, 2, 3], ['abc', {}], [123]]
assert filter_integers(test_values) == [5, 1, 2, 3]
```