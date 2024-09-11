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
    # Use list comprehension to filter out integers from the input list
    # The isinstance function checks if a value is an instance of a particular class
    # In this case, we're checking if the value is an instance of the int class
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```