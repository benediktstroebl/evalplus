```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Example function test
def test_filter_integers(values):
    assert filter_integers(values) == [5]

# Example 1: Filter only integer
values1 = [1, 2, 3, 'abc', {}, []]
test_filter_integers(values1)  # Pass

# Example 2: Filter empty list
values2 = []
test_filter_integers(values2)  # Pass

# Example 3: Filter non-integer
values3 = [1, 2, 3, 'a']
test_filter_integers(values3)  # Fail: [ ['a']] is not an integer
```