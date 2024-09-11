```markdown
### Filtering Integers from a List

This script defines a function `filter_integers` that takes a list of any type of Python objects and returns a new list containing only the integers.

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): The list of values to filter

    Returns:
        List[int]: A new list containing only the integers

    Example:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

### Explanation

The `filter_integers` function uses a list comprehension to iterate over the input list `values`. For each value, it checks if the value is an instance of the `int` type using the `isinstance` function. If the value is an integer, it is included in the new list. The resulting list of integers is then returned.

This solution is concise, readable, and efficient, making it a good fit for this problem.