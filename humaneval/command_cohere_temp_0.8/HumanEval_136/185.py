```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The function `largest_smallest_integers` uses the `min` and `max` functions with a custom key to find the smallest positive and largest negative integers in the list, respectively.

Here is a test suite to ensure the function behaves as expected:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, -5)
    assert largest_smallest_integers([1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == (-1, 5)
```

The test suite covers various scenarios, including lists with no negative or positive integers, only negative integers, and lists with both positive and negative numbers.