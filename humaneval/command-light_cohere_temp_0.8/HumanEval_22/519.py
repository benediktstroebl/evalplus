Here is a Python script with a self-contained function that solves the problem of filtering integers from a list:

```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values1 = [1, 2, 3, 'abc', 5]
assert filter_integers(values1) == [1, 2, 3]

values2 = [1, 2, 3, 4, 'five', 6]
assert filter_integers(values2) == [1, 2, 3, 4]

values3 = [1, 2, 3, ' ABC', 7]
assert filter_integers(values3) == [1, 2, 3]

values4 = [1, 2, 3, '2014', 7]
assert filter_integers(values4) == [1, 2, 3]

values5 = [1, 2, 'three', 3]
with pytest.assert2 invalid=True:
    assert filter_integers(values5) == [1, 2, 'three', 3]
```

This script provides a function `filter_integers` that accepts a list of values and returns a new list that contains only the integers from the original list. The test cases demonstrate the