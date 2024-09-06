```python
from typing import List

def filter_integers(values:
    """
        result = [x for x in values if isinstance(x, int)]
        return result
    """

def test():
    assert filter_integers(['a', 3.14, 5]) == [5], "Error 1"
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3], "Error 2"
    return
```