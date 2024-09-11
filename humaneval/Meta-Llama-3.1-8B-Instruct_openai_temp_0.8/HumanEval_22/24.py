### Filtering Integers from a List of Mixed Values
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list containing mixed types of values.

    Returns:
    List[int]: A list containing only integers from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of mixed values as input and returns a list containing only the integers from the input list. The function uses a list comprehension to iterate over the input list and checks each value using the `isinstance` function to see if it's an integer. If it is, the value is included in the output list.