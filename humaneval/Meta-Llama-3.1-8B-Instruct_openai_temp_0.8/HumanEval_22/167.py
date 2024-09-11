```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list of any Python values.

    Returns:
    List[int]: A list of integers from the input list.

    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Use list comprehension to filter integers from the input list
    return [x for x in values if isinstance(x, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any Python values as input and returns a new list containing only the integers from the input list. The function uses a list comprehension with the `isinstance` function to check if each value is an integer before including it in the output list. The script then tests the function with two example inputs.