```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with known good inputs and known bad inputs
values_good = [5, 3, 'three', (1, 2)]
values_bad = [1, 2, 'abc', {}]

assert filter_integers(values_good) == [5, 3, 'three']
assert filter_integers(values_bad) == []
```
This script defines a function **`filter_integers`** that accepts a list of values and returns a new list containing only the integers from the original list. It also provides a testing of the function with different inputs: good integers and bad characters.