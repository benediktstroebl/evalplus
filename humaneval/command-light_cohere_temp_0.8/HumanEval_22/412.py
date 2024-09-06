```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases 

values_test = [1, 2, 3, 'abc', 4, 5, 6, 7]
expected_test = [1, 2, 3, 4, 5]

values_list = ['a', 3.14, 5]
expected_list = [5]

result_test = filter_integers(values_list)
assert result_test == expected_list, "Filter failed."
```