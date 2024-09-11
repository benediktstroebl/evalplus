```markdown
### Filter Integers from a List
#### A Python Script to Filter Integers from a List of Any Python Values

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values: A list of any python values

    Returns:
        A list of integers

    Example:
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

This script uses list comprehension to filter the input list and return a new list containing only the integers. The `isinstance()` function is used to check if each value is an instance of `int`.
```