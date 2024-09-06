```python
from typing import List
def filter_integers(values: 
    return [x for x in values if isinstance(x, int)]
):
    pass

# Test
def test_filter_integers():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
```