```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list of any python values.

    Returns:
        List[int]: A list containing only the integers from the input list.
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This script uses list comprehension and the `isinstance` function to filter the input list for integers. The `isinstance` function checks if a value is an instance of a particular type, in this case `int`. The list comprehension iterates over the input list and includes only the values that are integers in the output list.