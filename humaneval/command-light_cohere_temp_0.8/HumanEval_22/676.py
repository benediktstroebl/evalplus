```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test = [['a', 3.14, 5], [1, 2, 'abc',}, [{}, []]]
print(filter_integers(values_test))

string_test = "abc"
print(filter_integers([string_test]))

empty_list_test = []
print(filter_integers(empty_list_test))

no_numbers_test = [1, 2, 'abc', 3.14]
print(filter_integers(no_numbers_test))
```