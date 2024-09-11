```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any python values

    Returns:
        List[int]: A list of integers
    """
    # Use a list comprehension to filter out integers from the given list
    # The isinstance(x, int) function checks if x is an integer
    return [x for x in values if isinstance(x, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```