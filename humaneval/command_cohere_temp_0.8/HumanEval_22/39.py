```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [val for val in values if isinstance(val, int)]
    return integers
```

The above code assumes the list of values input as a parameter `values` and returns a list of integers by using a list comprehension that filters out values that are not instances of the `int` class. 

Here is a simple test suite to verify the functionality of the `filter_integers` function:
```python
def test_filter_integers():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([0, 'abcd', 7.8, 4.0, 'efgh', 10.12]) == [0, 7, 4, 10]
```