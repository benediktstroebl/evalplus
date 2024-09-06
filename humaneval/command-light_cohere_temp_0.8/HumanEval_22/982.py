```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test
test_values = [1, 2, 3, 'abc', {}, [0]]
result = filter_integers(test_values)
assert [x for x in result if x !=()] == [1, 2, 3]
```