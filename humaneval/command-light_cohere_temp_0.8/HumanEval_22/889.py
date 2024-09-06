Here's a self-contained Python function that filters out integers from a list of various types:
```python
from typing import List, Any

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values = ['a', 3.14, 5]
test_filter = filter_integers(test_values)
assert len(test_filter) == 3

# Test case 2
test_values = [1, 2, 3, 'abc', {}, []]
test_filter = filter_integers(test_values)
assert len(test_filter) == 3

# Test case 3
test_values = List[1, 2, 3, 'abc', {}, []]
test_filter = filter_integers(test_values)
assert len(test_filter) == 3
```
This code defines a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. It uses the covered code type inference to check the input types and returns the filtered list of integers.