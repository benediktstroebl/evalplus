```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers

    Args:
        values (List[Any]): List of potential values, including non-integers and integers

    Returns:
        List[int]: List of filtered integers
    """
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 3, 'abc', 5, 6, '7', 8]
print(filter_integers(values))  # Output: [1, 2, 3, 5, 6, 8]
```