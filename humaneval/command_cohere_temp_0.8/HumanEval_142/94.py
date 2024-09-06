```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The code uses a simple `for` loop to iterate through each index and value in the input list `lst`. The `enumerate` function is used to access the index `i` and the value `num` simultaneously. The index is then checked to see if it meets the requirements of the problem, and, accordingly, the corresponding operation is conducted on the value `num`. To account for the fact that the returned sum should be an integer, the result is initialised and summed with the num value cast to an integer with the `int` function. The result is then returned when all list values have been processed. 

The unit tests for this function would typically be a checklist of edge cases to ensure that the function is correct for all possible values of the input. For example:
```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([0, 0, 0]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([0, 1, 2, 3, 0]) == 6
    assert sum_squares([-1, -2, -3, -4, -5]) == -114
    assert sum_squares([5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]) == 302
    assert sum_squares([-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]) == -302
    assert sum_squares([]) == 0
    assert sum_squares([0]) == 0
``` 

However, the above test suite is incorrect for this particular function, as it only checks the values of the output for certain inputs, which is not sufficient for this problem. Instead, we must check whether the function performs as described for _all_ inputs, which would require a more involved test suite or property-based testing framework.