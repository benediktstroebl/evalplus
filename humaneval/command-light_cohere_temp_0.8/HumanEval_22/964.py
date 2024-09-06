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
      File "<string>", line 3, in <module>
        raise ValueError("Invalid value: 'abc'. Expected one of str or int")
    ValueError: Invalid value: 'abc'. Expected one of str or int
    """
    if not all(isinstance(value, (int, float)) for value in values):
        raise ValueError("Invalid value: Expected one of str or int")
    return [int(value) for value in values if isinstance(value, int)]
```