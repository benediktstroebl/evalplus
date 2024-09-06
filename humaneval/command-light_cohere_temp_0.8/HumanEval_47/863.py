```python
def median(lst):
    """Return the median of the list lst."""
    if len(lst) < 1:
        return None
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test suite
def test_median():
    """Function to test the median function."""
    lst = [-10, 4, 6, 1000, 10, 20, 1, 2]
    assert median(lst) == 5.0
    lst2 = [10, 20, 4, 6, 1]
    assert median(lst) == 2.0
    lst3 = [1, 2, -10, 3, 4]
    assert median(lst) == 3.0
    lst4 = [10, 20, 4, -10, 6, 1]
    assert median(lst) == 5.0
```

This script defines a function `median` that computes the median of a list. The `test_median` function tests the `median` function with a variety of input lists to ensure it is working correctly.