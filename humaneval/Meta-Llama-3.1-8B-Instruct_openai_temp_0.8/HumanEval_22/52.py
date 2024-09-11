```markdown
### Integer Filter Script

This Python script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the original list.

#### Code

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): List of any Python values

    Returns:
        List[int]: List of integers from the original list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers([1, 2, 3, 'abc', {}, []]))
print(filter_integers(['a', 3.14, 5]))
```

#### Explanation

The `filter_integers` function uses a list comprehension to iterate over the input list `values`. It checks each value using the `isinstance` function to see if it's an integer. If it is, the value is included in the new list. The function then returns this new list of integers.

This script includes docstrings to provide documentation for the function and examples of usage. The comments explain how to use the function and provide context for the code. The example usage at the end demonstrates how to use the function with different inputs.