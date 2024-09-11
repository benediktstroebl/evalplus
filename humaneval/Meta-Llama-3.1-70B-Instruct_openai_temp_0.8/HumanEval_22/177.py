```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.
    
    Args:
        values (List[Any]): A list containing any python values.
    
    Returns:
        List[int]: A list of integers filtered from the input list.
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any python values, filters out the integers, and returns them as a new list. The function uses a list comprehension to achieve this.

The `isinstance(value, int)` function checks if a given value is an integer. If it is, the value is included in the new list. The test cases at the end of the script verify that the function works correctly.