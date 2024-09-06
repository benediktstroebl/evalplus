```python
from typing import List

def filter_integers(values):
    """
    Filter given list of any python values only for integers.

    Args:
        values: list of any python value

    Returns:
        list of integers
    """
    return [x for x in values if isinstance(x, int)]

# test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', }, []]
test_result = filter_integers(test_values)
print(test_result)  # Output: [5, 1, 2, 'abc']
```