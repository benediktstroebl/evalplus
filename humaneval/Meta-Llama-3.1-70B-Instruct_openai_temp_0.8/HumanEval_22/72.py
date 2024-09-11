```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list containing any type of python values
    
    Returns:
        List[int]: A list containing only integers from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Outputs: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Outputs: [1, 2, 3]
```

This script uses list comprehension to iterate over the input list `values`. It checks each value to see if it is an instance of the `int` type using the `isinstance` function. If a value is an integer, it is included in the new list that is returned. The `isinstance` function is used instead of simply checking `type(value) == int` to account for potential subclassing of the `int` type.