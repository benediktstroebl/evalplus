```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
The function `next_smallest()` sorts the input list of integers and retrieves the second-smallest element, returning `None` if the list has less than two elements. This method ensures consistent and efficient retrieval of the second-smallest value, handling edge cases where the list might be empty or have only one or two elements. 

Here's a testing framework to validate the `next_smallest` function:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None
    assert next_smallest([2, 1, 1, 11, 2, 22, 3, 3, 4]) == 3
    assert next_smallest([100, 1, 1, 1, 1, 2, 2000, 2000, 2001]) is None
``` 

To execute the test suite, navigate to the directory containing the test.py file and execute the following command:
```python
python test.py
``` 

This will run the test suite, and afterward, you'll see either a pass or failure confirmation, contingent upon the result of the tests. 

The `test_next_smallest()` function uses the `assert` statement to verify that the output of `next_smallest()` is correct for each case. Adjust the test suite as needed to cover additional scenarios and ensure the function's robustness and accuracy.  This testing framework is an essential component for validating your code and ensuring its correctness, allowing you to have confidence in the function's behavior and its handling of various scenarios.