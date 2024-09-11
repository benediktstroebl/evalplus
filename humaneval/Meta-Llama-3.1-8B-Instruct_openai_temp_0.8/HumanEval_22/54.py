```markdown
### Filtering Integers from a List of Mixed Values

This script defines a function `filter_integers` that filters a given list of mixed Python values and returns a new list containing only the integers.

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of mixed Python values

    Returns:
        List[int]: A new list containing only the integers from the input

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


# Example usage
if __name__ == "__main__":
    mixed_list = ['a', 3.14, 5]
    integer_list = filter_integers(mixed_list)
    print(integer_list)  # Output: [5]

    mixed_list = [1, 2, 3, 'abc', {}, []]
    integer_list = filter_integers(mixed_list)
    print(integer_list)  # Output: [1, 2, 3]
```

This script uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance(x, int)` function checks if each value `x` is an integer before including it in the new list.
```