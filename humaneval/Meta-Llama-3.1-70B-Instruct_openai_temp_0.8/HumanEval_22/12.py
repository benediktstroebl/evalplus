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
    return [value for value in values if isinstance(value, int)])

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Should print: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Should print: [1, 2, 3]
```

This script defines a function `filter_integers` that uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance(value, int)` condition checks if a value is an integer. The test cases at the end demonstrate the function's behavior.