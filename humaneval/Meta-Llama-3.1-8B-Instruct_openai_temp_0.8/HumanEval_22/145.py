```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers

    Args:
        values: A list of any python values.

    Returns:
        A list of integers filtered from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
values = ['a', 3.14, 5]
filtered_values = filter_integers(values)
print(filtered_values)  # Output: [5]

values = [1, 2, 3, 'abc', {}, []]
filtered_values = filter_integers(values)
print(filtered_values)  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any Python values as input and returns a new list containing only the integers from the original list. It uses a list comprehension to iterate over the input list and check if each value is an instance of `int` using the `isinstance` function. The filtered list of integers is then returned. The script also includes example usage of the function to demonstrate its behavior.