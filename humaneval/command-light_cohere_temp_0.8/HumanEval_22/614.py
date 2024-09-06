```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test the function
values = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, [], 0]
assert filter_integers(values) == [5, 3, 1, 2, 0], "Invalid filter"

# Another test with invalid values
values = [1, 2, 3, 'abc', {}, []]
assert filter_integers(values) == [], "Expected empty list"
```