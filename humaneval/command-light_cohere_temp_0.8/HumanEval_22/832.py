```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with known correct results
values_test = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
result_test = filter_integers(values_test)
assert result_test == [1, 2, 3, 5]
```