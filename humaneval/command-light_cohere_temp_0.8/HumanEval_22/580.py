```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

#Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([4, 2., '123']))  # []
print(filter_integers([1, 2, 3, 4, 'abc', [1, 2], [3, 4], []]))  # [1, 2, 3, 4]
```