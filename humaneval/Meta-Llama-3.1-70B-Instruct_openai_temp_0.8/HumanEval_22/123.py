```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list containing any python values.
    
    Returns:
        List[int]: A list containing only integers from the input list.
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]

# Additional test cases
print(filter_integers([]))  # Expected output: []
print(filter_integers([1, 2, 3, 4, 5]))  # Expected output: [1, 2, 3, 4, 5]
print(filter_integers(['a', 'b', 'c']))  # Expected output: []
print(filter_integers([True, False, None]))  # Expected output: []
```

This script defines a function `filter_integers` that uses a list comprehension to filter the input list and only include values that are instances of the `int` type. The `isinstance` function is used to check the type of each value. The function is then tested with several test cases to ensure its correctness.