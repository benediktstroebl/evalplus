```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The function `largest_smallest_integers` uses the `min` and `max` functions with a custom key to find the smallest positive and largest negative integers in the list, respectively.

Here is a test suite to ensure the full functionality of the function:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (7, 1)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([]) == (None, None)
```

The test suite includes three tests, one for each example provided in the problem statement.