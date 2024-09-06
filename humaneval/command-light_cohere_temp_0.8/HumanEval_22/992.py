```python
from typing import List
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

print(filter_integers(['a', 3.14, 5])) # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []])) # [1, 2, 3]
print(filter_integers([1, 2, 'abc', [], [1, 2]]))  # [1, 2]
print(filter_integers([1, 2, 3.a])) # ['a', 3]
print(filter_integers([1, 2, 3, 'abc', [], [1, 2], [3]]))  # [1, 2, 3]
```