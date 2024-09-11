```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any type of python values.

    Returns:
        List[int]: A list of integers filtered from the input list.
    """
    # Use list comprehension to filter integers
    # The isinstance function checks if a value is an instance of a class or a subclass thereof.
    # The int type is used to check for integers.
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values, filters out only the integers using list comprehension and the `isinstance` function, and returns the resulting list of integers. The script also includes test cases to demonstrate the function's behavior.