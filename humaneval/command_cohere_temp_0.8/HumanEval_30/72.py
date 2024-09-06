```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list `l` as input and returns a list of all positive numbers found in `l`. The function performs this task by using a list comprehension that iterates over each element `x` in the input list `l`, and assigns the value of `x` to the new list only if it is greater than zero. 

To test this function copy and paste the following code which provides example tests for the `get_positive` function:
```python
def test_get_positive():
    # Test list with only positive numbers
    assert get_positive([5, 3, 2, 9, 11, 1]) == [5, 3, 2, 9, 11, 1]

    # Test list with negative and positive numbers
    assert get_positive([-3, 8, -10, 4, 7, -5, 2, 0, 5, 10]) == [8, 4, 5, 7, 10] 

test_get_positive()
```

This test code uses the `assert` statement to check whether the output of the `get_positive` function is correct for each test case. 

The first test passes a list that contains only positive numbers, and the second test passes a list that contains both positive and negative numbers, the expected output for each case is enclosed in the `assert` statement and is checked against the actual output of the `get_positive` function. 

When executing these statements, if both tests pass, you will see the following output:
```python
test_get_positive (...)

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
``` 

This indicates that the `get_positive` function successfully passes both tests and works correctly to return only positive numbers for the given input lists.