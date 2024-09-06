```python
from typing import List

def filter_integers(values:
    """
        result = [int(x) for x in values if x.isdigit()]
       
    filter = lambda x: isinstance(x, int) and x >= 0
    return result

values = [3.14, 5, 'abc', 1, 2, '123']
print(filter_integers(values))
```