```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers
    Returns: List[int]"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    [],  # [] -> []
    ['a'],  # ['a'] -> []
    [1, 2, 3],  # [1, 2, 3] -> [1, 2, 3]
    [1, 2, 'abc'],  # [1, 2, 'abc'] -> []
    [1, 2, {}]  # [1, 2, {}] -> []
]

# Assertions
assert(test_filter_integers == [[]], "Should return [] for empty list")
assert(test_filter_integers == ['a']) ,"Should return [] for non-integer")
assert(test_filter_integers == [1, 2, 3]) ,"Should return [1, 2, 3] for integers")
assert(test_filter_integers == [1, 2, 'abc']) ,"Should return [] for non-integer")
assert(test_filter_integers == [1, 2, {}]) ,"Should return [] for empty object")
```