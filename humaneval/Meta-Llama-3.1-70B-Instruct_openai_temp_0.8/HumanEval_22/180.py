```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any type of python values

    Returns:
        List[int]: A list of integers filtered from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This script defines the `filter_integers` function as per the given specification. It takes a list of any Python values, filters out the integers using a list comprehension, and returns the filtered list. The `isinstance` function is used to check if a value is an integer. The script also includes test cases to verify the correctness of the function.