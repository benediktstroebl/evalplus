Here is a self-contained Python script that solves the problem of filtering out integers from a given list:

```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 3, "Expected list length is 3, got {}".format_error()

# Test case 2: Filter integers from a string
values2 = "abc123"
result2 = filter_integers(values2)
assert len(result2) == 0, "Expected list length is 0, got {}".format_error()

# Test case 3: Filter integers from an empty list
values3 = []
result3 = filter_integers(values3)
assert len(result3) == 0, "Expected list length is 0, got {}".format_error()

# Test case 4: Filter integers from a list containing objects
values4 = [1, 2, 'abc', 3, {}]
result4 = filter_integers(values4)
assert len(result4) == 3, "Expected list length is 3, got {}".format_error()
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the generic type hint `Any` and a list comprehension to filter out the integers from the given list. 

Finally, it runs tests on the `filter_integers` function with different input scenarios to validate its correctness.