```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values1 = [1, 2, 3, 'abc', 5]
test_result1 = filter_integers(test_values1)
assert [x for x in test_result1 if x == int(x)] == [1, 2, 3]

# Test case 2
test_values2 = [1, 2, 3, 'a', 5]
test_result2 = filter_integers(test_values2)
assert [x for x in test_result2 if x == int(x)] == [1, 2, 3]

# Test case 3
test_values3 = [1, 2, 'abc', 5, 3. a few integers, some strings]
test_result3 = filter_integers(test_values3)
assert [x for x in test_result3 if isinstance(x, int)] == [1, 2]
```
This Python code defines a function called filter_integers that filters out any non-integer values from a given list of values. It employs the specific typing to ensure the function's effectiveness.