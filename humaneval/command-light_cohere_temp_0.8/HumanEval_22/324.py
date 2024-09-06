```python
from typing import List
def filter_integers(values): 
    return [x for x in values if type(x) == int]

# Test cases for function
values_test = [['a', 3.14, 5], [1, 2, 'abc', [], {}]
assert filter_integers(values_test) == [5, 3, 1, 2]

```