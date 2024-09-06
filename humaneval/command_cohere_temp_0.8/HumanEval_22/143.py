```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It does so by using a list comprehension that checks if each element `x` in the input list `values` is an instance of the `int` class, i.e., `isinstance(x, int)`. The elements that satisfy this condition are added to the `result` list.

The function is self-contained and can easily be copied and pasted into a Python environment to test out different input lists. 

To run tests in a more structured manner, you could integrate this function into a unit testing framework like `pytest`. You can simply run `pytest` in your terminal, and it will automatically discover test functions and run them. To define a test function for `filter_integers`, you can use `pytest`'s native test discovery mechanism like so:
```python
# test_filter_integers.py
import pytest
from filter_integers import filter_integers  # assuming filter_integers is defined in a file called filter_integers.py

def test_filter_integers():
    # Integers present in the list remain unaffected by the filter
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]

    # Only integers present in the list are returned by the filter
    assert filter_integers([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]

    # Non-integer elements are filtered out
    assert filter_integers([1, 2, 'abc', 3, 4, 5]) == [1, 2, 3, 4, 5]

```

To execute these tests, first ensure that both the `test_filter_integers.py` and `filter_integers.py` files are in the same directory. Then, run `pytest` in the terminal at that directory, and it should discover and run these tests. 

This way, you can ensure that the function behaves correctly according to different scenarios.