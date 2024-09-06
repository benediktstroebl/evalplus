```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

print(filter_integers(['a', 3.14, 5])) # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []])) # [1, 2, 3]
print(filter_integers([10, 11, 'a', 123, 9, '8' as str])) # [10, 11]
```
This function, `filter_integers`, accepts a list of values and returns a new list containing only the integers present in the original list. The function uses the filter in Python, which checks whether each element in the list is an instance of a particular class.