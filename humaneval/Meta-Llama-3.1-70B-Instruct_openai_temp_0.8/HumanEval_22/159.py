```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any type of python values.

    Returns:
        List[int]: A list containing only integers from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """

    # Use list comprehension to filter the input list
    # The 'isinstance' function checks if a value is an instance of the given type
    # In this case, we're checking if each value is an instance of the 'int' type
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # Should print: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Should print: [1, 2, 3]
```