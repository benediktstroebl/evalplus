```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, converts it to a set to remove duplicates, and then sorts the resulting set before returning it. The sorted function is stable, meaning that it maintains the relative order of equal elements. Therefore, the original order of equal elements is preserved.

The set data structure in Python does not maintain any order. However, in Python 3.7 and later, sets maintain the insertion order, which is why the order of equal elements is preserved when converting the list to a set and then sorting it. 

For Python versions earlier than 3.7, you might want to use an OrderedDict from the collections module, which maintains the order in which elements were inserted. Here's how you can modify the function for Python versions earlier than 3.7:

```python
from collections import OrderedDict

def unique(lst: list) -> list:
    """Return sorted unique elements in a list"""
    seen = OrderedDict()
    for element in lst:
        seen[element] = None
    return sorted(seen.keys())

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```