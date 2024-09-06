```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test the function with various input types
values_test = [['a', 3.14, 5], [1, 2, 'abc', [], {}]
filtered_test = filter_integers(values_test)

assert filtered_test == [5, 3, 1, 2]
assert not filtered_test[0]

```