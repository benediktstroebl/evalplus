```python
from typing import List, Any
import doctest

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

if __name__ == "__main__":
    doctest.testmod()
```

This script uses a list comprehension to filter out non-integer values from the input list. The `isinstance(value, int)` function checks whether a given value is an integer. The result is a new list containing only the integer values from the input list. The `doctest` module is used to run the doctests embedded in the docstring. If the script is run directly (not imported as a module), it will run the tests.