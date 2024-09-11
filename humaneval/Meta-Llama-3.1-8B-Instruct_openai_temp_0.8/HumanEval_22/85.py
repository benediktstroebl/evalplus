```markdown
### Filter Integers from a List
#### Self-Contained Python Script

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any python values

    Returns:
    List[int]: A list of integers from the input list

    Examples:
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
This script defines a function `filter_integers` that takes a list of any python values and returns a new list containing only the integers from the original list. The function uses a list comprehension to iterate over the input list and filter out values that are not integers. The `isinstance` function is used to check if each value is an instance of the `int` type. Finally, the script includes example usage of the function to demonstrate its behavior.