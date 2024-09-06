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
    assert filter_integers([0, 'foo', 5.5, '7', 'foo']) == [0, 5]
``` 

The function `filter_integers` takes a list of values of any type and returns a list of integers that are present in the input list. The function iterates through each value in the input list and checks if it is an instance of the integer class using the `isinstance` function. If it is, the value is appended to the `integers` list and returned once the loop is finished. 

The test module `[test_filter_integers]` contains two test cases:
1. Test case `assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]` checks that the function `filter_integers` correctly filters the list having only integers among other values. 
2. Test case `assert filter_integers([0, 'foo', 5.5, '7', 'foo']) == [0, 5]` checks that the function `filter_integers` does not alter non-integer values. 

These tests verify that the function behaves as expected with different inputs.