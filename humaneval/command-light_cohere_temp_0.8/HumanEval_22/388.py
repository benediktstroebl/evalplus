```python
from typing import List

def filter_integers(values:
        return [x for x in values if type(x) == int]

filter_integers(['a', 3.14, 5])  # ['5']
filter_integers([1, 2, 3, 'abc', {}, []])  # [1, 2, 3]
```