```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list containing any type of python values.

    Returns:
    List[int]: A list containing only integers from the input list.
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```
This script uses a list comprehension to filter out non-integer values from the input list. The `isinstance(value, int)` condition checks whether each value is an instance of the `int` type, and if so, it's included in the output list.