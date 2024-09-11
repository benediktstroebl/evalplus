### Filter Integers from List
#### Script to Filter Integers from List of Any Python Values

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): List of any python values

    Returns:
    List[int]: List of integers from the input list

    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Example usage:
if __name__ == "__main__":
    # Test cases
    print(filter_integers(['a', 3.14, 5]))  # Output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that uses a list comprehension to filter the input list for integers. The `isinstance` function is used to check the type of each value in the list. If the value is an integer, it is included in the output list. The script also includes example usage and test cases to demonstrate the function's behavior.