Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, thus achieving the desired result of incrementing each element by 1. 

To confirm the functionality of the solution, you can write tests as follows:
```python
def test_incr_list():
    # Basic tests
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

    # Edge cases
    assert incr_list([0, 0, 0]) == [1, 1, 1]
    assert incr_list([-5, 0, -11, -1]) == [0, 1, -10, 0]

    # Long list
    large_list = [x for x in range(1000)]
    assert incr_list(large_list) == [x + 1 for x in range(1000)]
```

This test suite covers both basic and edge cases to ensure that the function appropriately handles a variety of input scenarios and correctly computes the increment.

You can run the tests individually using `test_incr_list()` or all at once using `python -m pytest` code.