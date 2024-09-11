```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list of any python values.

    Returns:
    List[int]: A list of integers filtered from the input list.
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Should print: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Should print: [1, 2, 3]
```

This script uses list comprehension to iterate over the input list and checks each value to see if it's an instance of the `int` class. If it is, the value is included in the output list. The `isinstance` function is used to check the type of each value, which is more Pythonic and efficient than using `type(value) == int`.