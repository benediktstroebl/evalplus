```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test case 1
values = ['a', 3.14, 5]
result = filter_integers(values)
assert len(result) == 3, "Failed test case 1"

# Test case 2
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
assert len(result) == 3, "Failed test case 2"

# Test case 3
values = [1, 2, 3]
result = filter_integers(values)
assert len(result) == 3, "Failed test case 3"
```
The code implements a function `filter_integers` that accepts a list of values and returns a new list containing only the integers from the input. It uses the specific testing by creating test cases that validate the correctness of the function with different sets of values.