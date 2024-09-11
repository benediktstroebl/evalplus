```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any type of python values

    Returns:
        List[int]: A list of integers from the input values
    """
    return [value for value in values if isinstance(value, int)]

# Example use cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

In this script, the `filter_integers` function uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance` function checks whether a value is an integer, allowing only integers to pass through to the output list. The docstring provides a detailed description of the function and its parameters, while the example use cases demonstrate its usage with different inputs.