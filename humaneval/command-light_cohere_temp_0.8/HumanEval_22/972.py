```python
from typing import List
def filter_integers(values:
    returns = List[int]
    return [num for num in values if num::int]

print(filter_integers(['a', 3.14, 5])) # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []])) # [1, 2, 3]
print(filter_integers([1, 2, 'hello', 3, 'world'])) # []
```