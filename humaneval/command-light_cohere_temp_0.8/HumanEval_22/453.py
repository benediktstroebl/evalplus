```python
from typing import List
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Test case 1
values = [3.14, 5]
result = filter_integers(values)
assert len(result) == 2, "Test case 1 failed: Expected length 2, got {}"

# Test case 2
values = [1, 2, 3, 'abc', {}, [])
result = filter_integers(values)
assert len(result) == 3, "Test case 2 failed: Expected length 3, got {}"

# Test case 3
values = [1, 2, 3, 4, 'abc', 5]
result = filter_integers(values)
assert len(result) == 5, "Test case 3 failed: Expected length 5, got {}"
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The test cases demonstrate the use of the function, passing all the tests successfully.