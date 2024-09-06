```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result

# Test cases
def test_filter_integers():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([4, 5, 6, 7, 8, 9, 10, 11, 12]) == [4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert filter_integers([13, 14, 15, 16, 17, 18, 19, 20, 21, 22]) == [13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

test_filter_integers()
```

The function `filter_integers` takes a list of any Python values as an argument and returns a list of integers. It uses a list comprehension to iterate over each value in the input list. If the current value is an integer, it is added to the result list. Finally, the function returns the result list containing only the integers from the original list.

The test cases ensure that the function correctly identifies and returns integers from various input lists, including lists with a combination of integer and non-integer values.