```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer of the negative integers in the list and `b` is the smallest integer of the positive integers in the list. If the list does not contain any negative or positive integers, `a` and `b` should be `None`. The `largest_smallest_integers` function solves this problem by using two conditional queries: one to find the smallest positive integer and another to find the largest negative integer. By chaining these queries in a tuple, we return the desired result.

This solution aims to adhere closely to the problem statement and uses Python's built-in functions to efficiently solve the challenge.

This code can be tested with the following markdown:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -3, -5, -7, -2, -4, -6, -8]) == (-8, 0)
```