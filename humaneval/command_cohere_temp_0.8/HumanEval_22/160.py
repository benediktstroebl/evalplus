```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It works by using a list comprehension that iterates over each value in the input list and checks if the value has `isinstance(x, int)` to see if it is an integer. If it is, the integer is included in the resulting list.

To follow the specified testing examples, the function can be called as follows:
```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
```