```python
from typing import List
def filter_integers(values):
    return [int(x) for x in values if x.isdigit()]
```
print(filter_integers(['a', 3, 'four', 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([0, -3, 'a', 'bc', 123]))  # Output: [123]
print(filter_integers([True, False, 'a']))  # Output: []
```