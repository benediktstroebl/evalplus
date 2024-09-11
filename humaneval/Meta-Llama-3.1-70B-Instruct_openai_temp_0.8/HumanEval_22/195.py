```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values: A list of any python values.

    Returns:
        A list of integers.

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

This script uses a list comprehension to filter out non-integer values from the input list. The `isinstance(value, int)` function checks if a value is an instance of the integer type. The filtered integers are then returned as a new list.