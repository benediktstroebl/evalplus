```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers

    Args:
        values (List[Any]): A list of values with potential elements of any type

    Returns:
        List[int]: A list containing only integers from the input list
    """
    return [num for num in values if isinstance(num, int)]

# Test the function with sample inputs and expected outputs
values_list = [3.14, 5, 'a', (1, 2), {'a': 1}, [], None]
result = filter_integers(values_list)
print(result)  # Output: [3.14, 5, 1, 2, {'a': 1}, []]
```