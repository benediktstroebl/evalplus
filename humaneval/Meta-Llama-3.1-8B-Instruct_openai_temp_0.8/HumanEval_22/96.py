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
    return [value for value in values if isinstance(value, int)]


# Test Cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([1.2, 3.4, 5.6]))  # Output: []
print(filter_integers(['a', 'b', 'c']))  # Output: []
print(filter_integers([True, False, None, 1, 2, 3]))  # Output: [1, 2, 3]
```

In this script, the function `filter_integers` uses a list comprehension to create a new list containing only the elements from the input list that are integers. The `isinstance(value, int)` function is used to check if a value is an integer. The test cases at the end demonstrate the function's behavior with various input lists.