```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

The function calls itself `filter_integers` which takes in a list of values and returns a list of integers. It uses a list comprehension to iterate over each value in the provided list and checks if the value is an instance of the integer class `isinstance(item, int)`. If it is, the value is included in the integer list. Finally, the function returns the integer list. 

This approach ensures that only integers are included in the resulting list, as specified by the problem statement.

The function is self-contained and does not rely on any external variables or functions, making it easy to use and integrate into larger projects. 

To demonstrate the functionality, here are some test cases that can be incorporated into the script:
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

    # Test case 3
    values = [0, 5, 'foo', 7.8, None, 123]
    expected = [0, 5, 123]
    result = filter_integers(values)
    assert result == expected

test_filter_integers()
```

To execute the tests, the code can start with calling the `test_filter_integers()` function. This will ensure that the `filter_integers` function is correct and behaves as expected.  This approach provides a robust and reusable way to filter lists and can be easily modified to handle different types of filtering requirements in future.