```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with a variety of data types
test_values = [['a', 3.14, 5, 1, 2, 'abc', {}, []]
test_results = filter_integers(test_values)

print(test_results)
```