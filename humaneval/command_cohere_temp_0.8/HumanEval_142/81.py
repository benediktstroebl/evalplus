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

The function sums over the list `lst` and for each entry it decides whether to square or cube the entry based on the value of `i % 3` and `i % 4`. The resulting sum is then returned. The edge case of an empty list is also handled as the example specifies. 

Below is a simple test suite for this function:
```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([0, 0, 0, 0, 0]) == 0
    assert sum_squares([10, 20, 30, 40, 50]) == 2586
```

This test suite can be added to a larger suite to consistently ensure functionality.