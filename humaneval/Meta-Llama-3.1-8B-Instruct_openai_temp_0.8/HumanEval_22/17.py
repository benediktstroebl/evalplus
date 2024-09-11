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
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([10, 'hello', 20.5, True]))  # Output: [10, 20]
```
This script defines a function `filter_integers` that takes a list of any python values and returns a new list containing only the integer values from the original list. The function uses a list comprehension to filter the values. The example usage at the end demonstrates how to use the function to filter integers from various lists.