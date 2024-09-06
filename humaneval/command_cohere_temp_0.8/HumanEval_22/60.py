```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The function `filter_integers` takes a list of values of any type as input and returns a list of integers. It uses a list comprehension to iterate over each element in the input list. For each element, it checks if it is an instance of the int class using the `isinstance()` function. If the check is true, the element is included in the resulting list. Finally, the function returns the list of filtered integers. 

This solution should help you achieve the problem statement to filter a list of various values (including integers) only to retain the integers.