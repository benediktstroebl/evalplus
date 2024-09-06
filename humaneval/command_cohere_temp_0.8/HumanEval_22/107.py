```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The above code directly addresses the problem statement by filtering `List[Any]` for elements that are instances of int using a list comprehension and the `isinstance` function.

To validate the functionality of the `filter_integers` function, you can use the following unit tests:
```python
def test_filter_integers():
    # Filters a list of various values, keeping only integers
    assert filter_integers(['a', 3.14, 5, 'foo' ]) == [5]

    # Filters a list of integers and other values
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]

    # Filters a list of only integers
    assert filter_integers([0, 2, 3, 4, 5]) == [0, 2, 3, 4, 5]

test_filter_integers()
```

Running the test file with `python test.py` would confirm that our function's behaviour corresponds to the problem statement and ensures its correctness.