```python
from typing import List
def filter_integers(values:
    return [int(el) for el in values if type(el) == int]

# Test
test_values = ['a', 3.14, 5]
result = filter_integers(test_values)
print(result)  # Output: [5]

# Test with list of strings
test_strings = ['1', 'abc', '2', '3']
result_strings = filter_integers(test_strings)
print(result_strings)  # Output: [1, 2, 3]

# Test with empty list
test_empty = []
result_empty = filter_integers(test_empty)
print(result_empty)  # Output: []
```