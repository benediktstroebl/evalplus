```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 20, 'abc', None]))  # []
print(filter_integers([1, 2, 3, '123']))  # [1, 2, 3]
```
This function, `filter_integers`, takes a list of values as input and returns a new list that contains only the integers from the input list. It uses the particular to filter the list of any python values only for integers.