```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of values that can be of any type

    Returns:
        List[int]: A list of integers

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script defines a function `filter_integers` that takes a list of any type of values as input and returns a list of integers. The function uses a list comprehension to iterate over the input list and check each value with the `isinstance` function to see if it's an integer. If it is, the integer is included in the output list. The script also includes two example test cases to demonstrate the function's behavior.