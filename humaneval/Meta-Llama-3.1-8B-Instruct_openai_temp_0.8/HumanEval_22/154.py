Here's a Python script that defines the `filter_integers` function:
```markdown
### Integer Filter Function

This script provides a function `filter_integers` to filter a list of any Python values and return only integers.

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any Python values

    Returns:
    List[int]: A list of integers from the input list

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance()` function checks if each value in the list is an instance of the `int` type. If it is, the value is included in the new list. Otherwise, it is skipped.