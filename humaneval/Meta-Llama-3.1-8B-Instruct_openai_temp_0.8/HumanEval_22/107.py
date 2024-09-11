### Integer Filter Script
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): The list of values to filter

    Returns:
    List[int]: A list containing only the integers from the input list

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

In this script, we define a function `filter_integers` that takes a list of any python objects as input. The function uses a list comprehension to iterate over the input list and checks each value using the `isinstance` function to see if it's an integer. If it is, the integer is included in the output list. The function returns this list of integers. The script also includes example usage of the `filter_integers` function.