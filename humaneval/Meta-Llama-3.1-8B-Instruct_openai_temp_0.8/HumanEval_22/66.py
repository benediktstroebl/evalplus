```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the original list. It uses a list comprehension with the `isinstance` function to check if each value is an integer. The example usage demonstrates the function's behavior with two different input lists.