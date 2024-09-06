```python
from typing import List

def filter_integers(values):
    """
    Filter given list for only integers.

    Args:
        values (List[Any]): The list of potential values to be filtered.

    Returns: List[int]: The list of integer values.
    """
    test_suitability():
    assert all(isinstance(value, int) for value in values),
        "All values must be integers!"
    return [value for value in values if isinstance(value, int)]

# Example usage
values = [1, 2, 3, 'abc', {}, 5]
result = filter_integers(values)
print(result)
```