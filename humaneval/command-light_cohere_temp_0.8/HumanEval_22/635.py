```python
from typing import List

def filter_integers(values:
    """Return integers from the list.

>>> values = ['a', 3.14, 5]
>>> filter_integers(values) == [5]
True
>>> values = [1, 2, 3, 'abc', {}, []]
>>> filter_integers(values) == [1, 2, 3]
True
```