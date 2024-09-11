```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any python values

    Returns:
        List[int]: A list of integers filtered from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script uses list comprehension and the `isinstance` function to filter the input list for integers. The `isinstance` function checks if an object is an instance of a particular class or a subclass of it. In this case, it checks if the object is an instance of the `int` class. The list comprehension then constructs a new list with only the elements that are integers.