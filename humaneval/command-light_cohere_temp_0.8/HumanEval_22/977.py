```python
from typing import List
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Test case 1
test_values = ['a', 3.14, 5]
result = filter_integers(test_values)
assert len(result) == 3, "Test case 1 failed"

# Test case 2
test_lists = [1, 2, 3, 'abc', {}, [])
result = filter_integers(test_lists)
assert len(result) == 4, "Test case 2 failed"

# Test case 3
test_objects = [1, 2, 3, {'a': 1, 'b': 2}, [1, 2, 3])
result = filter_integers(test_objects)
assert len(result) == 5, "Test case 3 failed"
```
This Python script defines a function `filter_integers` that filters a list of any values and returns a new list containing only the integers. The script then passes three test cases to the function and verifies the expected behavior.