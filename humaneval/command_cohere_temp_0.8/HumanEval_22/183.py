```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It does so by using a list comprehension that checks if each item `item` in the input list `values` is an instance of the `int` class, and if so, it includes the item in the `int_list`. The resulting `int_list` is then returned. 

To help understand the purpose of the function, the documentation above provides examples of test cases that can be used to verify the function's behavior. These examples illustrate how the function can be used to filter a list of values, highlighting the inclusion of only integer-type elements in the output. 

```python
def test_filter_integers():
    """
    Test the filter_integers function.
    """
    # Included integers in the input list are preserved
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]

    # Only integer values are retained
    assert filter_integers(['a', 3.14, 5]) == [5]
```

The test cases demonstrate how the function handles different scenarios, ensuring that it correctly filters out non-integer values from the list and retains only the integer-type elements.  By providing these test cases, users can verify the functionality of the function and gain confidence in its reliability.  In this case, the test cases are minimal and could not cover all the edge cases; however, they are sufficient to validate the function's behavior against the problem statement.  The given code coverage is acceptable given the simplicity of the function and the problem statement.  If the application required more stringent testing, more comprehensive testing strategies would be needed.