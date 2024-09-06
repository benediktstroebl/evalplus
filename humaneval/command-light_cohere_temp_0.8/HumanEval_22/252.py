```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values_test = [1, 2, 3, 'abc', {}, [0, 1, 2, 3, '4', True]]
print(filter_integers(values_test))  # Output: [1, 2, 3, 0, 1, 2, 3]

strings = ['a', 3.14, 'abc', (None)]
ints = [1, 2, 3]
combined = values_test + strings
print(filter_integers(combined))  # Output: [1, 2, 3, 3.