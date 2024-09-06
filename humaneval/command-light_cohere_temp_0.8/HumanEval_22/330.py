```python
from typing import List
def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test the function with known good inputs and known bad inputs
values_good = [5, 3, '12', (1, 2)]
values_bad = [1, 2, 'three', {}]

assert filter_integers(values_good) == [5, 3, 12]
assert filter_integers(values_bad) == []
```