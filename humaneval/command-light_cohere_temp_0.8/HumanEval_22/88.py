```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

print(filter_integers(['a', 3.14, 5]))  # ['5']
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 20, 'hello', 30, 40, 'abc']))  # [30, 40]
```