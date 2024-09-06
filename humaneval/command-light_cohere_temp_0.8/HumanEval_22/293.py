```python
from typing import List

def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test cases
values_test = [
    'a', 3.14, 'abc', 5, 1, 2, 3, [], None
]

print(filter_integers(values_test))  # [5] expected output
```