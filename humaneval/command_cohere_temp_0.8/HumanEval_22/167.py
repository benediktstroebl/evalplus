```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [val for val in values if isinstance(val, int)]

# Tests
assert filter_integers(['a', 3.14, 5]) == [5]
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
``` 

This code uses a list comprehension to iterate over each value in the input list `values`, and checks if each value is an instance of the `int` class using the `isinstance()` function. For each integer value, it includes it in the new list, and skips non-integer values. 

The tests assert that the function correctly filters out only the integer values from two different lists that include strings, floats, and integers. 
```python
# Tests
assert filter_integers(['a', 3.14, 5]) == [5]
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
```