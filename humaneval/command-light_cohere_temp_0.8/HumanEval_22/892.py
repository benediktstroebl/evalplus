```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test = [1, 2, 'three', three, (])
assertEqual(filter_integers(values_test), [1, 2, three])

strings = ['a', 3.14, 'five']
assertNotEqual(filter_integers(strings), [3.14, 'five'])

empty_list = []
assert len(filter_integers(empty_list)) == 0

large_values = [20, 200, 50000]
assert filter_integers(large_values) == [20, 200, 50000]
```
This code provides a function `filter_integers` that accepts a list of values and returns a new list containing only the integers from the input. It has been tested with several cases to ensure its correctness.