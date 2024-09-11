Here's a self-contained Python script that solves the given problem:

```markdown
### Filter Integers from a List of Python Values

#### Problem Description

This script defines a function `filter_integers` that filters a given list of any Python values and returns a new list containing only the integers from the original list.

#### Code

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
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

#### Explanation

The `filter_integers` function uses a list comprehension to iterate over the input list and includes only the values that are instances of `int`. The `isinstance` function checks if a value is an instance of a given class (in this case, `int`). The resulting list of integers is returned by the function. The script also includes example usage of the `filter_integers` function to demonstrate its behavior.