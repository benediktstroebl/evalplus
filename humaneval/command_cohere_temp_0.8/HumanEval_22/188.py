```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [val for val in values if isinstance(val, int)]
    return integers
```

The function calls itself `filter_integers()` which takes in a list of values of any type `List[Any]` and returns a list of integers `List[int]` by using a list comprehension that filters out non-integer values using the `isinstance()` function. 

To verify the functionality of the function, you can use the following tests:
```python
def test_filter_integers():
    # Positive test cases
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([3, 9, 'string', True, None, 42]) == [3, 9, 42]

    # Negative test cases
    assert filter_integers([1, 2, 'abc', 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([1, 2, None, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([]) == []
```

These tests cover different scenarios, including edge cases, to confirm that the function correctly filters out non-integer values from the list.