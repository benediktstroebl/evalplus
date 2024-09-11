```python
def unique(l: list):
    """
    Return sorted unique elements in a list

    Args:
        l (list): Input list of elements

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we use the built-in `set` function to remove duplicates from the list and the `sorted` function to sort the resulting set in ascending order. The `set` function automatically removes duplicates because it only stores unique elements. The `sorted` function then sorts these unique elements in ascending order and returns them as a list. 

Note that this script does not preserve the original order of elements in the input list, as sets are inherently unordered data structures. If you need to preserve the original order, you can use an OrderedDict from the `collections` module instead:

```python
from collections import OrderedDict

def unique_ordered(l: list):
    """
    Return ordered unique elements in a list

    Args:
        l (list): Input list of elements

    Returns:
        list: Ordered list of unique elements

    Example:
        >>> unique_ordered([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [5, 3, 2, 9, 0, 123]
    """
    return list(OrderedDict.fromkeys(l))

# Test the function
print(unique_ordered([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This version of the function uses an OrderedDict to preserve the original order of elements in the input list.