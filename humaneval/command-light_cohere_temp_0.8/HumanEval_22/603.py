```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

values = ['a', 3.14, 5, 1, 2, 'abc', {}, [], 0]
test_values = [values, values[:] + [10], values[::-1]]
test_values_result = filter_integers(test_values)
test_values_list = list(test_values_result)

print("Test Values:", test_values_list)
print("Expected Output:", [int] + test_values_list)

values_only = filter_integers(['a', 3.14, 5])
print("Filtering integers:", values_only)
```