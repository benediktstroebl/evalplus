```python
from typing import List
def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', }, [(), [5]]

test_results = [filter_integers(test_values[0]), filter_integers(test_values[1]), filter_integers(test_values[2])]

print(test_results)  # [['a', 3, 5], [1, 'abc', ], [(), []]
```