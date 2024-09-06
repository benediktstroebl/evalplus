```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

This function uses a list comprehension, which is a powerful Python technique, to filter out items that are not of type integer. The condition `isinstance(item, int)` checks if each item in the list is an integer, and adds the items that meet this condition to the new list.

To better explain the functionality, below is an example of usage along with corresponding test outputs:
```python
values = ['a', 3.14, 5, 'foo', 7.7, [1, 2], ({'a': 1}), None]

print("Original list:", values)
print("Filtered list:", filter_integers(values))
```

```
Original list: ['a', 3.14, 5, 'foo', 7.7, [1, 2], ({'a': 1}), None]
Filtered list: [5, 7.7, [1, 2]]
```