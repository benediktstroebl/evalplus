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

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

In this script, we define a function `filter_integers` that uses a list comprehension to iterate over the input list `values`. The `isinstance(x, int)` function is used to check if each element `x` is an integer; if it is, the element is included in the output list. The function returns the filtered list of integers. 

The example usage at the end of the script demonstrates how to use the `filter_integers` function with different inputs.