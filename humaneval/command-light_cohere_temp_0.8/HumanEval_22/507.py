```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

values = ['a', 3.14, 5]
result = filter_integers(values)
print(result)  # Output: [5]
```