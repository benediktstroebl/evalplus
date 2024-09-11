```markdown
### Filter Integers from a List of Any Python Values
#### Solution in Python

This script uses a list comprehension to filter out non-integer values from a given list.

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): List of any python values

    Returns:
        List[int]: List of integers from the input

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

This code defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integer values. It uses a list comprehension to create the new list, iterating over the input list and including a value in the new list only if it is an instance of `int`. The function is then tested with two example inputs.