```python
from typing import List

def filter_integers(values):
    return [int(x) for x in values if x.isinstance(int)]

# Tests
def test_filter_integers():
    values = [1, 2, 3, 'abc', 5, 6]
    
    expected = [1, 2, 3]
    got = filter_integers(values)
    
    assert expected == got
```