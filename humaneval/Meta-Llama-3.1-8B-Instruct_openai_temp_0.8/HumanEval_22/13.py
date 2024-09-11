```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any python objects

    Returns:
        List[int]: A list of integers from the input list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test the function
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
    print(filter_integers([3.14, 'abc', []]))  # []
    print(filter_integers([1, 2, 3.5, 4, 5]))  # [1, 2, 4, 5]
```

This script defines the `filter_integers` function, which uses a list comprehension to filter out non-integer values from the input list. The `isinstance(value, int)` function checks if each value in the list is an instance of the `int` type. The function returns a new list containing only the integer values. The script also includes example test cases to demonstrate the function's behavior.