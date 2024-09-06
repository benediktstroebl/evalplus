```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [val for val in values if isinstance(val, int)]
    return integers
```

The above code assumes the following tests:
```python
def test_filter_integers():
    # Type hinting: List with only int type
    values = [1, 2, 3, 'abc', {}, []]

    expected = [1, 2, 3]
    result = filter_integers(values)

    assert result == expected
```

The function `filter_integers()` takes a list of values of any type and returns a list of integers. It does so by using a list comprehension that checks if each value in the input list is an instance of the `int` class, and if so, includes it in the new list. The resulting list comprehension is returned. 

The function is well-documented with a docstring that explains its purpose, parameters, and return value.