```python
from typing import List

def filter_integers(values):
    """
    Filter given list of any python values only for integers.

    Args:
        values: list of any python value

    Returns:
        list: list of integers
    """
    return [x for x in values if isinstance(x, int)]

# Example usage
values_list = [1, 2, 3, 'abc', {}, 5]
print(filter_integers(values_list))  # Output: [1, 2, 3]
```
This code defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. The function uses a filter method to create the new list.