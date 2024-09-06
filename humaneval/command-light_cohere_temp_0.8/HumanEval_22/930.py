```python
from typing import List
def filter_integers(values:
    """ Return list of integers only """
    result = [x for x in values if isinstance(x, int)]
    return result

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', [], None]
test_results = [filter_integers(values) for values in test_values]

print("Test Cases:", test_values)
print("Results:", test_results)
```