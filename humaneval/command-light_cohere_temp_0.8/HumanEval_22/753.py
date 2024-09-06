```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers
    :param values: list of any python object
    :return: list of int
    """
    return [num for num in values if isinstance(num, int)]

# Test the function
test_values = [1, 2, 3, 'abc', True, [0, 1, 'two', 3]]
filtered = filter_integers(test_values)
print(filtered)  # Expected output: [1, 2, 3, True, [0, 1, 'two', 3]]
```