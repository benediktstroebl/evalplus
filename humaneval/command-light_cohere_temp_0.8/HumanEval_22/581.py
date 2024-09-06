```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    >>> filter_integers([1, 2, 'abc'])
    Traceback (most recent call last):
      File "<stdin>", line 7, in <module>
    File "<stdin>", line 4, in filter_integers
    File "<stdin>", line 2, in List
    File "<stdin>", line 1, in values
    File "<stdin>", line 5, in filter_integers
    TypeError: unsupported operand type '[' or ']' found for comparison
    """
    values = [int(x) for x in values if x.isdigit()]
    full_values = [x for x in values if isinstance(x, int)]
    return full_values
```