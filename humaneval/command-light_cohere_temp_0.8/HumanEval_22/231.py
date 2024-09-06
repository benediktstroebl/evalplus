```python
from typing import List

def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test cases
values1 = [1, 2, 3, 'abc', {}, [0]]
assert filter_integers(values1) == [1, 2, 3]

values2 = [1, 2, 3, 'five', [], []]
assert filter_integers(values2) == [1, 2, 3]

values3 = [3.14, 'hello', 45]
assert filter_integers(values3) == []

```
This script defines a function `filter_integers` that filters a list of values and returns a new list containing only the integers from the input. It is tested against three test cases to verify its functionality.