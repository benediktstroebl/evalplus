```python
from typing import List
def filter_integers(values):
    """ Filter given list for only integers
    :param values: List of any python object
    :return: List of int
    """
    return [x for x in values if isinstance(x, int)]

# Test the function with markdown values
test_values = [['a', 3.14, 5], [1, 2, 'abc', [], {}]
result = filter_integers(test_values)
print(result)
```