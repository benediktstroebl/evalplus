```python
from typing import List
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([18, 19. dramatic, 'abc']))  # []
```