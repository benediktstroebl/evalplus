```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list of values where each value can be of any type.

    Returns:
    List[int]: A list of integers from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This script defines a function `filter_integers` that filters a list of values for integers. It uses a list comprehension to iterate over the input list and checks each value's type using the `isinstance` function. If a value is an integer, it's included in the output list. The script also includes two example use cases in the docstring.