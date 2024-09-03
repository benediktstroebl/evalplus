```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: A list of integers contained in the input list.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Tests
def test_filter_integers():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([None, 5, None]) == [5]

if __name__ == "__main__":
    test_filter_integers()
```

The function `filter_integers` takes a list of values and returns a list of integers, omitting non-integer values. Two tests are defined to validate the behavior of the function with different input scenarios. The `test_filter_integers` function calls `filter_integers` with the provided test cases and compares the result with the expected `[int]` output.  The `if __name__ == "__main__":` block ensures that the test functions are executed only when the script is run directly. 

This code demonstrates a basic use of the `isinstance` function to identify and filter integers in a list, providing a straightforward approach to solving the problem.