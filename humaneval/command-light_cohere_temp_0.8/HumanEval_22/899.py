```python
from typing import List
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test cases for function
test_filter = []
test_filter.add([List([1, 2, 3, 'abc', {}, [5], [6.14]]))
assert filter_integers(test_filter) == [1, 2, 3, 5, 6]
test_filter.add([List([-1, 0, '2', 3, 'four', []]))
assert filter_integers(test_filter) == [0, 3, 'four']
test_filter.add([List([10, 20, 'hello']))
assert filter_integers(test_filter) == [10, 20]
```