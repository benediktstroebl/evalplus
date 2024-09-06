```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

values = [3.14, 5, 1, 'abc', []]
result = filter_integers(values)
print(result)
```