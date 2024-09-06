```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test the function
values = [1, 2, 3, 'abc',{}, []]
print(filter_integers(values))  # [1, 2, 3]

values = [3.14, 5]
print(filter_integers(values))  # [5]

values = List[Any]()
print(filter_integers(values))  # []
```