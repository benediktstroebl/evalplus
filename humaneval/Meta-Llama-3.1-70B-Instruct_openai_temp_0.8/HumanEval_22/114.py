```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
    values (List[Any]): A list containing any type of python values
    
    Returns:
    List[int]: A list containing only the integers from the input list
    """
    # Use list comprehension to filter the input list for integers
    # The isinstance() function checks if an object (first argument) is an instance or subclass of a class (second argument)
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
print(filter_integers([]))  # Expected output: []
print(filter_integers([None, True, False]))  # Expected output: []
```