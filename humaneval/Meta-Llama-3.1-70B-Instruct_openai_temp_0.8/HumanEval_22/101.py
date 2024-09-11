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

# Example use cases:
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any python values as input and returns a new list containing only the integers from the original list. The function uses a list comprehension to achieve this. The `isinstance` function is used to check if each value in the list is an integer. The script also includes example use cases to demonstrate the function's behavior.