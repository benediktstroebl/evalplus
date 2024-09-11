```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list containing any python values.

    Returns:
    List[int]: A list of integers filtered from the input list.
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

In this script, the `filter_integers` function uses a list comprehension to iterate over the input list and includes only the values that are instances of the `int` type. The `isinstance` function checks if an object is an instance or subclass of a class. This approach provides a concise and readable solution to the problem.