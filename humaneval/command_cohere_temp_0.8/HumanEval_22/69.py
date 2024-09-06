```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The `filter_integers` function takes a list of values of any type and returns a list of integers. It works by creating a new list with the same values as the input list, but with one key difference: it includes only the elements that are instances of the integer class from the `isinstance` check. Finally, it returns the new list filtered in this way. 

This function solves the problem of filtering a list of variables of different types and only keeping the integers, as demonstrated by the example use cases in the original problem statement. 

```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
``` 
The example use cases demonstrate the function's ability to filter out non-integer values from a list containing a mixture of integer and non-integer values, leaving only the integers in the list.