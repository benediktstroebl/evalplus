```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any python values

    Returns:
    List[int]: A list containing only the integers from the input list
    """
    return [value for value in values if isinstance(value, int)]


# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

In this script, we use a list comprehension to iterate over each value in the input list `values`. We use the `isinstance` function to check if the value is an integer. If it is, we include it in the output list. The `isinstance` function checks if an object is an instance or subclass of a class. In this case, we're checking if the value is an instance of the `int` class.