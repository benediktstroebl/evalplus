```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers
    Returns list with only integers
    """
    return [num for num in values if isinstance(num, int)]

# Tests
def test_filter_integers():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([1, 2, 'abc', 3]) == []
```