```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The `filter_integers` function takes a list of values of any type as input and returns a list of integers. It utilizes Python's list comprehension to iterate over each value in the input list. For each value, it checks if the value is an instance of the int class using the `isinstance()` function. If the condition is met, the value is included in the resultant list.

Here is an example usage of the function:
```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
```

This will filter out the non-integer values ('a', 3.14, 'abc', {}, []) and only include the integers (1, 2, 3, 5).