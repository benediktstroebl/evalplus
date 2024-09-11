Here's a Python function to solve the problem:

```markdown
### Filter Integers from a List

This script filters a given list of any Python values to only include integers.

#### Code
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any Python values

    Returns:
        List[int]: A list of integers

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]
```

#### Usage
You can use this function to filter any list containing various types of values. The function uses a list comprehension to create a new list containing only the integers from the original list.

```python
values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
filtered_integers = filter_integers(values)
print(filtered_integers)  # Output: [5, 1, 2, 3]
```

This function is a simple and efficient way to filter out non-integer values from a list. It uses the built-in `isinstance` function to check if a value is an integer before including it in the new list.