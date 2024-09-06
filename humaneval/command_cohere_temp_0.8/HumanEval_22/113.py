```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [value for value in values if isinstance(value, int)]
    return integers
```

The function calls itself `filter_integers()` which takes in a list of values of any type `List[Any]` and returns a list of integers `List[int]` using a list comprehension that filters out values not instance of int (`isinstance(value, int)`). 

To keep the function robust, we can add tests like:
```python
def test_filter_integers():
    # Basic tests:
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]

    # Edge case: Empty list:
    assert filter_integers([]) == []

    # Edge case: Single item:
    assert filter_integers([7]) == [7]

    # Edge case: List with many different types:
    assert filter_integers([None, 42, 3.14, 'foo', [1, 2, 3], {}]) == [42]
``` 

This way the function is tested against different types of lists, edge cases, and different types of values contained in the list, ensuring its correctness.