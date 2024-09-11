```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of python values of any type.

    Returns:
        List[int]: A list of integers from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

In this script, we define a function `filter_integers` that takes a list of any python values as input. We use a list comprehension to iterate over the input list, and include only the values that are instances of `int`. The result is a new list containing only the integers from the original list. We then test the function with the provided examples.