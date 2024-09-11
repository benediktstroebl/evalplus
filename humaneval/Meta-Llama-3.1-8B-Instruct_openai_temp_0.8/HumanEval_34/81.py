```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we're using the built-in Python `set` data type to remove duplicates from the list. Since a set in Python is an unordered collection of unique elements, we use `sorted()` function to sort the list before returning it. 

However, as noted in the docstring, this function does not preserve the original order of elements. If you need to preserve the order, you could use an OrderedDict from collections module, like so:

```python
from collections import OrderedDict

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = OrderedDict()
    for elem in l:
        seen[elem] = None
    return sorted(seen.keys())

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```