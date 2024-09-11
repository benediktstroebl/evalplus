Here is a Python script that defines the `filter_integers` function:
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```
This script defines a list comprehension that filters the values in the input list only for integers, and returns a new list containing only the integers. The `isinstance(x, int)` check is used to determine whether a value is an integer.

You can run this script to test the `filter_integers` function. The `print` statements at the end will output the expected results.

**Note:** This script uses Python 3.6+ syntax (specifically, the `List[Any]` type hint) and the `isinstance(x, int)` function to check if a value is an integer. If you're using an earlier version of Python, you may need to adjust the script accordingly.