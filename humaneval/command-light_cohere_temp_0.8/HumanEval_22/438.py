```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 20, 30, 40, 50, 60, ' Intro to Python'])))  # [10, 30, 40, 50]
```