```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list as an argument, aiming to process integer entries in the list based on their indices' divisibility by 3 and 4. When the index is a multiple of 3, the function squares the integer; if the index is a multiple of 4 but not of 3, it cubes the integer. The entries' indices not being a multiple of 3 or 4 are left unchanged. The function then returns the sum of all entries. 

The `enumerate` loop is used to iterate through the list, exploiting the `i` index to access the index `num` value, thereby applying the specified transformations.

To validate the functionality, you can test the function with various input lists. Here is a test code:
```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6, "Failed example 1"
    assert sum_squares([-1, -5, 2, -1, -5]) == -126, "Failed example 2"
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 30, "Failed example 3"
    assert sum_squares([-2, -4, -1, -3]) == -44, "Failed example 4"
    assert sum_squares([0, 0, 0, 0]) == 0, "Failed example 5"
    assert sum_squares([-1, 2, 3, -4, 5, -6]) == -132, "Failed example 6"
```

The expected outcome for each test case is stated in the assertion, serving as a benchmark for the `sum_squares` function's correctness. 

When you run the file, the test suite will automatically execute using the `test_sum_squares` function, providing you with feedback on whether the function behaves as expected on different inputs.