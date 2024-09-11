### Integer Filter Script

The following Python script provides a function `filter_integers` to filter a list of any Python values and return a new list containing only the integers.

```markdown
### Code
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any Python values

    Returns:
        List[int]: A list containing only the integers from the input list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Example usage:
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

### Explanation

*   The `filter_integers` function uses a list comprehension to create a new list containing only the integers from the input list.
*   The `isinstance(value, int)` function is used to check if a value is an integer.
*   The function takes a list of any Python values as input and returns a list of integers.
*   The script includes example usage to demonstrate how to use the `filter_integers` function.