```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The above code assumes the list could contain any Python value including strings, numbers, integers, floats, collections, etc. It uses a list comprehension with the `isinstance()` function to filter out only integers from the list. 

To run the code simply run:
```python
filter_integers(['a', 3.14, 5])
filter_integers([1, 2, 3, 'abc', {}, []])
```

The code passes the test cases as described in the original problem.