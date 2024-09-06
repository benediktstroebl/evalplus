```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: List of integers contained in the input list.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Tests
def test_filter_integers():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([4, 5, 6, 7, 8, 9, 'abc', 'def', 10, 11, 12]) == [4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert filter_integers(['a', 3.14, 5]) == [5]

test_filter_integers()
```

The function `filter_integers` takes a list of values as input and returns a list of integers that are present in the input list. It achieves this by iterating through each value in the input list and checking if it is an instance of the `int` class using the `isinstance()` function. If it is an integer, it is added to the `integers` list, which is returned at the end of the function. 

Two tests are provided to validate the functionality of the `filter_integers` function. These tests verify the correct filtering of integers for a variety of input lists.