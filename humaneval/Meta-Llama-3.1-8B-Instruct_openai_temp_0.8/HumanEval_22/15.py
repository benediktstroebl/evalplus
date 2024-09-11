```markdown
### Filtering Integers from a List of Python Values
#### Solution

We can use a list comprehension to filter out integers from a list of any Python values.

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): List of any python values

    Returns:
        List[int]: List of integers from the input list

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
### Code Explanation

*   We use a list comprehension to create a new list containing only the integers from the input list.
*   The `isinstance(value, int)` function checks if the current value is an integer. If it is, the value is included in the new list.
*   The resulting list of integers is returned by the function.