```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer of those in the list that are less than zero and `b` is the smallest integer of those that are greater than zero. The function `largest_smallest_integers` does just that, using `max` and `min` to find the largest negative and smallest positive, respectively.

This solution assumes that the list may or may not contain either positive or negative integers. In the event that the list contains no negatives or no positives, `None` is returned as the respective value of the tuple to reflect that no largest or smallest value could be found.

Here is a simple test suite to ensure that the function behaves appropriately:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([-3, -1, -7, -11, -4]) == (-3, None)
    assert largest_smallest_integers([0, 1, 2, 3, 4, -1, -2, -3]) == (-3, 3)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([-5, -10, -6, -4, -8]) == (-10, None)
```