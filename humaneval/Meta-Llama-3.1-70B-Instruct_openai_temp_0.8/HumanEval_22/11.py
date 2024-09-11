```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any python values

    Returns:
        List[int]: A list containing only integers from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Example use cases:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that uses a list comprehension to filter the input list for integers. The `isinstance` function checks if a value is an instance of the `int` type, and if so, it is included in the output list.

You can run this script to see the example use cases in action. The function is well-documented with a docstring that explains its purpose, parameters, and return values.