```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_results = [filter_integers(values) for values in test_values]

print(test_results)
```