```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num = num ** 2
        if i % 4 == 0 and i % 3 != 0:
            num = num ** 3
        result += num
    return result
```

The function sums over the list and for each entry multiplies the element by its squared or cubed value depending on the index criteria. The resulting sum is then returned. The function is reusable and can be invoked with different lists to test. 

The code includes tests that verify the function behavior for the examples described in the problem statement:
```python
# Test the sum_squares function
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

test_sum_squares()
```

Thus, the function's correctness is confirmed by the test suite.  It is reusable and can be used with other lists to get the sum of squares and cubes of the elements.