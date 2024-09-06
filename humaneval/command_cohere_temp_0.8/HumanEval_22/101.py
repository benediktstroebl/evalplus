```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_values = [item for item in values if isinstance(item, int)]
    return int_values
```

The function calls the built-in `isinstance()` function, which checks if each list item has a type of `int`. The `filter_integers()` function accepts a list of values of any type and returns a list that includes only the items that have a type of `int`. It utilizes list comprehension, which allows for creating a new list by applying an expression to each item in the existing list. The expression used is `isinstance(item, int)`, which returns `True` if the item is an integer, and `False` otherwise. After generating lists of `True`es and `False`es, it filters out the `True` values from the list using list comprehension, leaving only the integers.  This technique allows the code to filter out any non-integer items in a single pass through the list, making it efficient.