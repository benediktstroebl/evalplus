```python
from typing import List

def filter_integers(values):
    return [int(i) for i in values if i.isinstance(str) and isinstance(str, int)]

filter_integers([1, 2, 3, 'abc', {}, []]) # [1, 2, 3]
filter_integers([1, 2, 3, 4, '123']) # [1, 2, 3, 4]
filter_integers([10, 20, 30]) # []
filter_integers(['a', 3.14]) # ['a', 3.14, 'hello']) # ['a', 3.14]
```