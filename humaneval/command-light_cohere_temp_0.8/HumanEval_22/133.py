```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# test suite
test_filter_integers = [
    ("Passed test: filtering non-integer values [['a', 3.14, 5]],",
    ("Failed test: filtering integer [1, 2, 'abc'],",)),
]
```  We have defined a function named `filter_integers` that takes a list of values as an argument and returns a new list that contains only the integers from the given list. This is function uses the filtering logic to filter out non-integer values and return only the integers from the list.