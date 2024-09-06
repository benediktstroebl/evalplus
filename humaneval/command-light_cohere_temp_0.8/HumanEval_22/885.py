```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

filter_integers(['a', 3.14, 5]) # [5]
filter_integers([1, 2, 3, 'abc', {}, []]) # [1, 2, 3]
```
This code defines a function `filter_integers` that filters out non-integer values from a given list. It uses the `ispy types` to check for integer values.