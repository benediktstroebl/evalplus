```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [i for i in values if isinstance(i, int)]

# Test cases
test_values = [
    ['a', 3, '56', (1), 'true'],
    [1, 2, 3, 'abc', {}],
]

test_results = [filter_integers(value) for value in test_values]

print(test_results)
 ```