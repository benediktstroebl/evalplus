```python
from typing import List
def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    >>> values = [1, 'abc', 3, 'abc', 5, (6))
    >>> filter_integers(values)
    [1, 3, 5]
    """
    return [x for x in values if isinstance(x, int)]

#Test the function
values = [1, 'abc', 3, 'abc', 5, (6)]
print(filter_integers(values))  # expected output: [1, 3, 5]
```