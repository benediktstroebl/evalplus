```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers
    :param values: list of any python value
    :return: list of integers
    """
    return [x for x in values if isinstance(x, int)]

# Test the function with some examples
values_test = [1, 2, 3, 'abc', 3.14, 5]
print(filter_integers(values_test))  # Output: [1, 2, 3, 3. however, ...
```