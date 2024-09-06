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
    assert filter_integers([100, 200, 300, 'abc', 404, None, [], ()]) == [100, 200, 300, 404]

if __name__ == "__main__":
    test_filter_integers()
```

The function `filter_integers` checks if each value in the input list is an integer, and if so, adds it to the returned list. The test cases ensure that the function behaves as expected for a variety of input lists.  Running the script will automatically test the function's behavior against the test cases.  This solution is structured and efficiently solves the problem statement.  It provides clear code comprehension, maintainability, and reusability due to the incorporation of type hints and test coverage.