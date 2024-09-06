```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers

    Args:
        values: list of any python value, can be objects, strings, numbers, etc

    Returns:
        list of integers
    """
    integers = [x for x in values if isinstance(x, int)]
    return integers

# test
values_test = [1, 2, 'three', three, [1, 2], [1, 2, three]]
result = filter_integers(values_test)
print(result)
```