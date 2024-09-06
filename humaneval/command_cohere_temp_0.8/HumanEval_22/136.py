```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The above code directly addresses the problem statement by filtering `List[Any]` for elements that are instances of int using a list comprehension and the `isinstance()` function.

To validate the functionality of the `filter_integers()` function, I would encourage you to write additional test cases, such as: 

```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
>>> filter_integers([0, None, 6, '999', -3.14, []])
[0, 6]
``` 

This would strengthen the script, providing an even greater level of assurance in its correctness. Let me know if you'd like me to write these additional tests to further optimize your code!