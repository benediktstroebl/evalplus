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

# Test cases
def test_filter_integers():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([100, 200, 300, 400, 500, 'foo']) == [100, 200, 300, 400, 500]

if __name__ == "__main__" :
    test_filter_integers()
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It iterates through each value in the input list and adds an integer value to the result list if the current value is an integer. The test suite verifies that the function correctly identifies and filters integers from the list, regardless of the list's content.