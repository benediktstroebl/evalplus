```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function
test_values = [1, 2, 3, 'abc', float('inf'), [0]]
result = filter_integers(test_values)
assert len(result) == 5, "Filter returned wrong number of integers"

test_empty_list = []
result = filter_integers(test_empty_list)
assert len(result) == 0, "Filter should have returned an empty list"

test_string = "Hello World"
result = filter_integers([test_string])
assert result == [], "Filter should return an empty list for non-numeric strings"

test_invalid = [['a', 3.14, 5]
result = filter_integers(test_invalid)
assert len(result) == 2, "Filter should have returned only integers"
```
This code defines a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. It uses the particular type to filter out non-integer values from the input list. This script also includes a series of tests to verify the correctness of the `filter_integers` function for different scenarios, such as empty lists, non-numeric strings, and lists containing only non-integer values.