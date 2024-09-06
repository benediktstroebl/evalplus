```python
from typing import List

def filter_integers(values):
    """Filter given list for only integers."""
    return [i for i in values if isinstance(i, int)]

# Test cases
test_filter_integers = [
    ['a', 3.14, 5], [1, 2, 'abc', None, [], {}], [1, 2, 3, 'abc', {}, []]
]

for test_case in test_filter_integers:
    actual_result = filter_integers(test_case)
    expected_result = [i for i in test_case if isinstance(i, int)]
    assert actual_result == expected_result, f"Test case [{test_case}] failed."
```