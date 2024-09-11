```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values: A list of any python values.

    Returns:
        A list of integers.
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script uses list comprehension to filter the input list. It checks each value to see if it is an instance of `int` using the `isinstance` function. If it is, it includes it in the output list. The test cases at the end verify that the function behaves as expected.