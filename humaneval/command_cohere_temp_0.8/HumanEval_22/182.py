```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: List of integers contained in the input list.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result

# Test cases
def test_filter_integers():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([4, 5, 6, 7, 8, 9, 'foo', 'bar']) == [4, 5, 6, 7, 8, 9]
    assert filter_integers([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

test_filter_integers()
```

The function `filter_integers` takes a list of any Python values as an argument and returns a list of integers present in the input list. It does so by iterating through each value in the input list and checking if the value is an instance of the integer class using the `isinstance` function. If it is, the value is added to the `result` list. The function returns the `result` list once all values have been checked.

The test cases ensure that the function correctly identifies and returns only the integer values from the input lists. 

You can add these test cases to a separate file called `test_filter_integers.py` and run them with the `python -m unittest test_filter_integers` command to verify the functionality of the code. 

You can also add this script to a file and run it with `python file_name.py`.  It can also be imported and used as a regular Python module, as it does not perform any global modifications that would require it to be in the main scope.