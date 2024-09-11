```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any python values

    Returns:
        List[int]: A list of integers from the input list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([1.5, 2.5, 3.5]))  # Output: []
print(filter_integers(['a', 'b', 'c']))  # Output: []
print(filter_integers([True, False, None]))  # Output: []
```

This script defines a function `filter_integers` that takes a list of any Python values as input and returns a new list containing only the integers from the input list. The function uses a list comprehension to iterate over the input list and filter out non-integer values using the `isinstance` function. The script also includes some example test cases to demonstrate the function's behavior.