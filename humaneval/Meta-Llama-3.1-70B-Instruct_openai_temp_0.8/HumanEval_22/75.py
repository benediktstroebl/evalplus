```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list of any python values.

    Returns:
        List[int]: A list of integers from the input list.
    """
    return [value for value in values if isinstance(value, int)]

# Example use cases:
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

In this script, the `filter_integers` function uses a list comprehension to iterate over the input list `values`. It checks if each value is an instance of `int` using the `isinstance()` function. If the value is an integer, it is included in the output list. The function returns a list of integers from the input list.