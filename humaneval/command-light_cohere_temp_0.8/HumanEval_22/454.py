```python
from typing import List

def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test cases
values_test = [1, 2, 3, 'abc', {}, [0, 1, 'two', 3])
assert filter_integers(values_test) == [1, 2, 3]

int_only_test = [1, 2, 3, 'four', 5]
assert filter_integers(int_only_test) == [1, 2, 3, 5]

non_int_test = ['abc', 'five', (7)]
assert filter_integers(non_int_test) == []
```
This script defines a function `filter_integers` that filters a list of values and returns a new list containing only the integers. The test cases demonstrate the both the expected results.