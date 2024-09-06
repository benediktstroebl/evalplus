```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers
    Args:
        values: list of any python value, can be mixed types

    Returns:
        filtered_ints: list of integers only
    """
    return [num for num in values if isinstance(num, int)]

# Test case 1
values1 = ['a', 3.14, 5]
filtered_ints1 = filter_integers(values1)
assert filtered_ints1 == [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
filtered_ints2 = filter_integers(values2)
assert filtered_ints2 == [1, 2, 3]

# Test case 3
mixed_values = [5, 'str', 'int', 'abc', True, [1, 2, 3], {4}]
filtered_ints3 = filter_integers(mixed_values)
assert filtered_ints3 == [5, int, 'abc', True, [1, 2, 3, 4]]
```