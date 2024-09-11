```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any python values.

    Returns:
        List[int]: A list of integers filtered from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

In this script, the `filter_integers` function uses a list comprehension to iterate over the input list `values`. It checks each value to see if it's an instance of `int` using the `isinstance` function, and if so, includes it in the output list. This approach provides a concise and readable solution to the problem.