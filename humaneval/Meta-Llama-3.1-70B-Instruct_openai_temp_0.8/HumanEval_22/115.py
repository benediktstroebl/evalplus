```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list containing any type of python values.

    Returns:
    List[int]: A list containing only the integers from the input list.
    """
    return [value for value in values if isinstance(value, int)]

# Example use cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```
This script uses list comprehension along with the `isinstance()` function to filter out integers from the input list. The `isinstance()` function checks if an object (in this case, each value in the list) is an instance or subclass of a class (in this case, `int`). If it is, the value is included in the output list.