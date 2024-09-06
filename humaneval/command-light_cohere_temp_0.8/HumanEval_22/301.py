```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [num for num in values if isinstance(num, int)]

# Test the function with different inputs
test_values = [1, 2, 3, 'abc', 3.14, [1, 2, 3, 4, 5, 6]]
test_output = filter_integers(test_values)
print(test_output)  # Output: [1, 2, 3, 3.TH
```