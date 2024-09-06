```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

values = ['a', 3.14, 5]
print(filter_integers(values))  # ['a', 3.14, 5]
```