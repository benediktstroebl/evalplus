```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any python values

    Returns:
        List[int]: A list containing only integers from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Example use cases:
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script uses list comprehension to create a new list that only includes the elements from the input list that are integers. The `isinstance(value, int)` function checks if a value is an instance of the `int` class, effectively filtering out non-integer values.