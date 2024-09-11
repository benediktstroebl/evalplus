```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
    values (List[Any]): A list containing any type of python values
    
    Returns:
    List[int]: A list containing only integers from the original list
    """
    # Use list comprehension to filter the list and keep only integers
    return [value for value in values if isinstance(value, int)]

# Example use cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script defines the `filter_integers` function as described in the problem statement. It uses list comprehension and the `isinstance` function to filter the input list and keep only the values that are integers. The function is then tested with the provided example use cases.