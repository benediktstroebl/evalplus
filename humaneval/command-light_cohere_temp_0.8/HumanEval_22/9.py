```python
from typing import List

def filter_integers(values:
    return [num for num in values if isinstance(num, int)]

filter_integers(['a', 3.14, 5]) # [5]
filter_integers([1, 2, 3, 'abc', {}, []])  # [1, 2, 3]
filter_integers([10, 'test'])  # []
```