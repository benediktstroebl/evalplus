```python
from typing import List

def filter_integers(values:
    """
        filtered = [x for x in values if isinstance(x, int)]
        return filtered
    """
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([10, 20, 30]) == [10, 20, 30]
    assert filter_integers([1, 2, 'three']) == []
```
The function `filter_integers` takes a list of values and returns a new list with only the integers from the original list. 
It uses a list comprehension and the `isinstance` function to filter out the non-integer values from the input list.