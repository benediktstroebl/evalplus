```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list of any python values.

    Returns:
        List[int]: A list of integers.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

In this script, the function `filter_integers` uses a list comprehension to iterate over each value in the input list. It checks if the value is an instance of `int` using the `isinstance` function. If it is, the value is included in the output list. The function then returns the list of integers.

The test cases at the end of the script demonstrate the function's behavior with the examples provided in the problem statement.