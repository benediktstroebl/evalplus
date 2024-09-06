```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [val for val in values if isinstance(val, int)]
    return integers
```

The function uses a list comprehension that iterates over each value in the input list values. It checks if each value isinstance(val, int), which returns True if the value is an integer, including both positive and negative integers. For all True values, it includes the corresponding value in the integers list. Finally, the function returns the integers list containing only the integers from the original input list. 

To follow best practices, the function includes a docstring that describes the purpose of the function, provides informative type hints, and uses the any Python data type for the return value to indicate that it may contain both positive and negative integers. 

Here is an example of how to test this function against a number of test cases to ensure that it behaves as expected:
```python
def test_filter_integers():
    # Positive test cases:
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([-1, 0, 1, 2, 3, 4, 5, 6]) == [-1, 0, 1, 2, 3, 4, 5, 6]

    # Negative test cases:
    assert filter_integers([1, 'a', 3, 'b', 5, 'hello']) == [1, 3, 5]
    assert filter_integers([1.5, 2, 3.0, 'abc', {}, []]) == []
```