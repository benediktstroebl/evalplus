```python
from typing import List

def filter_integers(values:
    """ Filters and returns only the integers from the input list"""
    filtered_int = [x for x in values if isinstance(x, int)]
    return filtered_int

# Example test cases
test_filter = [
    assert filter_integers(['a', 3.14, 5]) == [5], "Failed to filter integers"
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3], "Failed to filter integers"
]

print("Tests passed!")
```