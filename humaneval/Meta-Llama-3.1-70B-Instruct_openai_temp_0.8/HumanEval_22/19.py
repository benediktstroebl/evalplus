```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list containing any python values
    
    Returns:
        List[int]: A list of integers from the input list
    """
    # Use list comprehension to filter out integers
    # The isinstance() function checks if an object (first argument) is an instance or subclass of a class (second argument)
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any Python values as input and returns a list containing only the integers from the input list. The `isinstance` function is used to check if each value is an integer, and list comprehension is used to create the filtered list. The script also includes test cases to verify the function's correctness.