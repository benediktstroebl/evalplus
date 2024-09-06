```python
from typing import List

def filter_integers(values:
    # Filter list for only integers
    return [x for x in values if type(x) == int]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', None], [(), [], [1, 2]]

test_cases = [
    ('filter_integers', test_values),
    ('filter_integers', [1, 2, 3, 'abc', {}]),
    ('filter_integers', []),
    ('filter_integers', [1, 2, 3])
]

# Run the function on each test case and check the results
for func, test in test_cases:
    assert func(test) == test_values
```