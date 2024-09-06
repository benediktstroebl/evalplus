```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Usage example:
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
print(result)  # Output: [1, 2, 3]
``` 

The `filter_integers` function takes a list of values of any type and returns a list of integers found in the input list. It does so by iterating through each value in the input list and checking if the value is an instance of the integer class. If it is, the value is added to the integers list, which is returned at the end of the function. The output in the example is `[1, 2, 3]`, as the integers `1`, `2`, and `3` are the only integers present in the input list. 

To see if the function behaves as expected, let's write a couple of test cases inspired by the ones you provided:
```python
def test_filter_integers():
    # Test case one
    test_list1 = ['a', 3.14, 5]
    expected1 = [5]
    result1 = filter_integers(test_list1)
    assert result1 == expected1

    # Test case two
    test_list2 = [1, 2, 3, 'abc', {}, []]
    expected2 = [1, 2, 3]
    result2 = filter_integers(test_list2)
    assert result2 == expected2

test_filter_integers()
``` 

The test cases will determine whether the behavior of the `filter_integers` function matches the expected behavior. If the test cases pass, it shows that the function works correctly.  In the code provided, the `test_filter_integers` function creates two test cases, each providing a list of values and the expected output resulting from applying the `filter_integers` function to the input. For each test case, `assert result == expected_result` checks whether the actual output matches the expected output.  If the conditions are met, it means that the function works as expected, and the `test_filter_integers` function passes. 

To execute the test cases, it is necessary to run the `test_filter_integers()` function at the end of the script.  The function calls `assert` to compare the actual and expected outputs, and outputs an error message if the values do not match.  If the tests pass, you will not see any output or error messages, as Python will only print traceback if the `assert` statement fails.  In that case, you will have to modify the function to ensure it behaves as expected.