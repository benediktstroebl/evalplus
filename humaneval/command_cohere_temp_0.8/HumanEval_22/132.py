```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It utilizes Python's list comprehension feature along with the `isinstance()` function to filter out non-integer elements from the input list. 

To ensure correctness, this function undergoes testing:
```python
def test_filter_integers():
    # Test case 1
    values = ['a', 3.14, 5]
    expected = [5]
    result = filter_integers(values)
    assert result == expected

    # Test case 2
    values = [1, 2, 3, 'abc', {}, []]
    expected = [1, 2, 3]
    result = filter_integers(values)
    assert result == expected

test_filter_integers()
```

The test cases check the function behavior against different input lists and ensure that the returned list contains only integers, verifying the function's correctness.